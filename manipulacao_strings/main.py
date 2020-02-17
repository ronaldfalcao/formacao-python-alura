from extrator import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=PESO&moedadestino=LIBRAS"

moedas = ExtratorArgumentosUrl(url)

print(moedas.retorna_moedas())
