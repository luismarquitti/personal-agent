import unittest
from unittest.mock import patch, MagicMock
import os
from app.core.database import get_db_connection

class TestDBConnection(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_get_db_connection_success(self, mock_connect):
        # Setup mock
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        
        # Call function
        conn = get_db_connection()
        
        # Assertions
        mock_connect.assert_called_once()
        self.assertEqual(conn, mock_conn)
        
    @patch('psycopg2.connect')
    def test_get_db_connection_failure(self, mock_connect):
        # Setup mock to raise exception
        mock_connect.side_effect = Exception("Connection failed")
        
        # Call function
        with self.assertRaises(Exception):
            get_db_connection()

if __name__ == '__main__':
    unittest.main()
