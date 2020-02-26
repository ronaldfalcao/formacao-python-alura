from extrator import ExtratorArgumentosUrl

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150"

print("Caso 1")
cambio = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = cambio.retorna_moedas()
valor = cambio.retorna_valor()
print(moedaOrigem, moedaDestino, valor)

print("\nCaso 2")
url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150"
cambio = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = cambio.retorna_moedas()
valor = cambio.retorna_valor()
print(moedaOrigem, moedaDestino, valor)
