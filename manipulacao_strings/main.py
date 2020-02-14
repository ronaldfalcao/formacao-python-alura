from extrator import ExtratorArgumentosUrl


url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar"

"""
---------------------Aula02

# Usar nas URLs find() e findall() para retornar os dois argumentos da URL

# usar o find() e findall() com o len() no slice

# Objetivo é buscar informações dos parâmetros da URL

class ExtratorArgumentoURL:
    def __init__(self,url):
        if self.stringEhValida(url):
            self.url = url
        else:
            raise LookupError(“Url inválida”)
    @staticmethod
    def stringEhValida(url):
        if url:
            return True
        else:
            return False
            
def retornaMoedas(self):
        buscaMoedaOrigem = "moedaorigem"
           buscaMoedaDestino = "moedadestino"

        inicioSubstringMoedaOrigem = self.encontraIndiceInicioSubstring(buscaMoedaOrigem)
        finalSubstringMoedaOrigem = self.url.find("&")
        moedaOrigem = self.url[inicioSubstringMoedaOrigem:finalSubstringMoedaOrigem]

           inicioSubstringMoedaDestino = self.encontraIndiceInicioSubstring(buscaMoedaDestino)
        finalSubstringMoedaDestino = self.url.find("&valor")
        moedaDestino = self.url[inicioSubstringMoedaDestino:finalSubstringMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicioSubstring(self, moedaOuValor):
            return self.url.find(moedaOuValor) + len(moedaOuValor) + 1

"""

"""
------------------Aula 03

Mostrar os problemas que vão acontecer quando muda a ordem dos parâmetros

def __init__(self, url):
        if self.stringEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError("url inválida!")
            
def verificaMoedaOrigem(self, buscaMoedaOrigem):
       self.url = self.url.replace("moedadestino", "real", 1)  # primeiro vou fazer sem o 1 e depois vou usa-lo
       inicioSubstringMoedaOrigem = self.encontraIndiceInicioSubstring(buscaMoedaOrigem)
    finalSubstringMoedaOrigem = self.url.find("&")
        return self.url[inicioSubstringMoedaOrigem:finalSubstringMoedaOrigem]
        
if moedaOrigem == "moedadestino":
            moedaOrigem = self.verificaMoedaOrigem(buscaMoedaOrigem)
            
def retornaValor(self):
        buscaValor = "Valor".lower()
        inicioSubstringValor = self.encontraIndiceInicioSubstring(buscaValor)
        valor = self.url[inicioSubstringValor:]
        return valor
        
Deixar na Main

from ExtratorArgumentosURL import ExtratorArgumentoURL
url =” https://www.bytebank.com.br/cambio?moedaorigem=real&moedadesino=dolar&valor=150”
cambio = ExtratorArgumentoURL(url)
moedaOrigem,moedaDestino=cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem,moedaDestino,valor)
Aqui ta tudo bem, teste agora o caso em que “moedaorigem=moedadestino”.
url =” https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadesino=dolar&valor=150”
cambio = ExtratorArgumentoURL(url)
moedaOrigem,moedaDestino=cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem,moedaDestino,valor)

"""

