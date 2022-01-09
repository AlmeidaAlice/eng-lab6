class Repeticao:

  def nome_mais_comum (self,lista):
    contador = 0
    palavra = lista[0]
    for i in lista:
        frquenciaAtual = lista.count(i)
        if (frquenciaAtual > contador+1):
            contador = frquenciaAtual
            palavra = i
            resposta = palavra , lista.count(i)
        if(contador == 0): 
            resposta = 'nada repete', lista.count(i)
            
    return resposta   

  def caractere_mais_comum (self,lista):
      resposta="";
      lista = str(lista)
      contador = 0
      palavra = lista[0]
      for i in lista:
          frquenciaAtual = lista.count(i)
          if (frquenciaAtual > contador):
              if (i != ',' and i!= ' ' and i!= '[' and   i!=']' and i!="'"):
                  contador = frquenciaAtual
                  palavra = i
                  resposta = palavra , lista.count(i)
      return resposta