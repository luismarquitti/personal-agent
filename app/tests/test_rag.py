import unittest
from unittest.mock import patch, MagicMock
from app.tools.rag_engine import add_iot_product, query_knowledge_base, update_knowledge_base

class TestRAGEngine(unittest.TestCase):

    def test_add_iot_product(self):
        """Testa inserção de produto IoT."""
        result = add_iot_product(
            name="Smart Bulb RGB",
            brand="HueLike",
            protocol="Zigbee",
            payload_yaml="on: true\nbrightness: 100",
            metadata={"version": "1.0"}
        )
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
        self.assertIn("id", result)

    @patch("app.tools.rag_engine.embeddings")
    def test_query_knowledge_base(self, mock_embeddings_obj):
        """Testa busca semântica (mockando objeto embedding)."""
        # Mock do método embed_query no objeto mockado
        mock_embeddings_obj.embed_query.return_value = [0.0] * 1536
        
        results = query_knowledge_base("como configurar zigbee?")
        self.assertIsInstance(results, list)
        mock_embeddings_obj.embed_query.assert_called_once()
        
    @patch("app.tools.rag_engine.PyPDFLoader")
    @patch("app.tools.rag_engine.embeddings")
    @patch("os.path.exists")
    def test_update_knowledge_base_mock(self, mock_exists, mock_embeddings_obj, mock_loader):
        """Testa pipeline de upload mockado."""
        mock_exists.return_value = True
        mock_embeddings_obj.embed_query.return_value = [0.1] * 1536
        
        # Mock do loader retornando 1 documento
        mock_doc = MagicMock()
        mock_doc.page_content = "Conteúdo de teste para RAG."
        mock_doc.metadata = {"page": 1}
        mock_loader.return_value.load.return_value = [mock_doc]
        
        result = update_knowledge_base("fake.pdf")
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
        mock_embeddings_obj.embed_query.assert_called()

if __name__ == '__main__':
    unittest.main()
