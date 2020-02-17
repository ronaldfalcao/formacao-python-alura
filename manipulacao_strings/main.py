from extrator import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=peso&moedadestino=libra"

moedas = ExtratorArgumentosUrl(url)

print(moedas.retorna_moedas())
