class ExtratorArgumentosUrl:

    def __init__(self, url):
        if self.url_eh_valida(url):
            self.url = url.lower()
        else:
            raise LookupError("url inválida!")

    @staticmethod
    def url_eh_valida(url):
        if url:
            return True
        else:
            return False

    def encontra_indice_inicio_substring(self, moeda_ou_valor):
        return self.url.find(moeda_ou_valor) + len(moeda_ou_valor) + 1

    def retorna_moedas(self):

        busca_moeda_origem = "moedaorigem"
        busca_moeda_destino = "moedadestino"

        inicio_substring_moeda_origem = self.encontra_indice_inicio_substring(busca_moeda_origem)
        final_substring_moeda_origem = self.url.find("&")
        moeda_origem = self.url[inicio_substring_moeda_origem:final_substring_moeda_origem]
        inicio_substring_moeda_destino = self.encontra_indice_inicio_substring(busca_moeda_destino)
        final_substring_moeda_destino = self.url.find("&valor")
        moeda_destino = self.url[inicio_substring_moeda_destino:]

        if moeda_origem == "moedadestino":
            moeda_origem = self.verifica_moeda_origem(busca_moeda_origem)

        return moeda_origem, moeda_destino

    def verifica_moeda_origem(self, busca_moeda_origem):

        self.url = self.url.replace("moedadestino", "real", 1)
        inicio_substring_moeda_origem = self.encontra_indice_inicio_substring(busca_moeda_origem)
        final_substring_moeda_origem = self.url.find("&")

        return self.url[inicio_substring_moeda_origem:final_substring_moeda_origem]

    def retorna_valor(self):
        busca_valor = "Valor".lower()
        inicio_substring_valor = self.encontra_indice_inicio_substring(busca_valor)
        valor = self.url[inicio_substring_valor:]
        return valor
