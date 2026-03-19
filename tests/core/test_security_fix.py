import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import importlib

# Mock cryptography and dotenv before importing crypto
sys.modules['cryptography'] = MagicMock()
mock_fernet_class = MagicMock()
sys.modules['cryptography.fernet'] = MagicMock(Fernet=mock_fernet_class)
sys.modules['dotenv'] = MagicMock()

class TestSecurityFix(unittest.TestCase):
    def setUp(self):
        mock_fernet_class.reset_mock()

    @patch('os.getenv')
    def test_encryption_key_missing_raises_error(self, mock_getenv):
        # Setup: ENCRYPTION_KEY is not set
        mock_getenv.return_value = None

        # Action & Verification: Importing or reloading the module should raise ValueError
        with self.assertRaises(ValueError) as cm:
            # Check if module is already imported, if not, import it
            if 'app.core.crypto' in sys.modules:
                importlib.reload(sys.modules['app.core.crypto'])
            else:
                import app.core.crypto

        self.assertEqual(str(cm.exception), "A variável de ambiente ENCRYPTION_KEY não está configurada.")

    @patch('os.getenv')
    def test_encryption_key_present_loads_and_encodes_correctly(self, mock_getenv):
        # Setup: ENCRYPTION_KEY is set as a string
        key_str = "G-8gK4Qn4qC2K9J6G-8gK4Qn4qC2K9J6G-8gK4Qn4qA="
        mock_getenv.return_value = key_str

        # Action
        if 'app.core.crypto' in sys.modules:
            importlib.reload(sys.modules['app.core.crypto'])
        else:
            import app.core.crypto

        # Verification
        # Fernet should have been called with the bytes version of the key
        mock_fernet_class.assert_called_once_with(key_str.encode())
        self.assertEqual(sys.modules['app.core.crypto'].ENCRYPTION_KEY, key_str)

if __name__ == '__main__':
    unittest.main()
