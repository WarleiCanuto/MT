import unittest
import random
from MT import aceitacao
palavras_teste = []

#palavras_teste.append('1100') Reprovada
#Quando o numero de 1s é maior ou igual a 6 o tempo de execução é alto

for p in range(20):
    palavras_teste.append('0'*random.randint(1, 5) + '1'*random.randint(1, 5))
print(palavras_teste)

class FuncTeste(unittest.TestCase):
    def test_aceitacao(self):
        for p in palavras_teste:
            self.assertTrue(aceitacao(p))

if __name__ == "__main__":
    unittest.main()
    #Lembrar de remover os prints para testar