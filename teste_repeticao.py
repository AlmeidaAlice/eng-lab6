import unittest
from repeticao import Repeticao


class TestRepeticao(unittest.TestCase):
  
  def testEmptyCaractere(self):
    lista = []
    caractere = Repeticao()
    self.assertEqual(caractere.caractere_mais_comum(lista), "")

  def test_caractere_1(self):
    caractere = Repeticao()
    self.assertEqual (caractere.caractere_mais_comum(['mamao','caju','mesa','pano','tango','olhar']), ('a', 7))

  def test_caractere_2(self):
    caractere = Repeticao()
    self.assertEqual (caractere.caractere_mais_comum(['caju','caju','caju','caju','caju','c']), ('c', 6))

  def test_caractere_3(self):
    caractere = Repeticao()
    self.assertEqual (caractere.caractere_mais_comum(['@c','#ma','!52','@hu','ciju','z']), ('@', 2))  

  def testNotEmptyCaractere(self):
    caractere = Repeticao() 
    self.assertNotEqual (caractere.caractere_mais_comum([' ']), ('ju', 2))

  def test_palavra_1(self):
    nome = Repeticao()
    self.assertEqual (nome.nome_mais_comum(['ju','ju','ka']), ('ju', 2))

  def testNotEmptyPalavra(self):
    nome = Repeticao() 
    self.assertNotEqual (nome.nome_mais_comum([' ']), ('sopa', 2))

  def test_palavra_3(self):
    nome = Repeticao()
    self.assertEqual (nome.nome_mais_comum(['caju','caju','caju','caju','caju','caju']), ('caju', 6))

  def test_palavra_4(self):
    nome = Repeticao()
    self.assertEqual (nome.nome_mais_comum(['@c','#ma','!52','@hu','ciju','z','@c']), ('@c', 2))

  def test_palavra_5(self):
    nome = Repeticao() 
    self.assertTrue (nome.nome_mais_comum(['lata','lata']), ('lata', 2))







