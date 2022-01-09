import unittest
from repeticao import Repeticao


class Test(unittest.TestCase):
  
  def testEmptyCaractere(self):
    lista = []
    caractere = Repeticao()
    self.assertEqual(caractere.caractere_mais_comum(lista), "")

  



