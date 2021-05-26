import unittest
    class TestClass(unittest.TestCase):

        def test_meu_metodo(self):
            self.assertEqual(valor_esperado , valor_real, "mensagem caso o teste falhe")

    if __name__ == "__main__":
            unittest.main()