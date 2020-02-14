class ExtratorArgumentosUrl():

    def __init__(self, url):
        if self.url_eh_valida(url):
            self.url = url
        else:
            raise LookupError("A URL passada não é válida.")

    @staticmethod
    def url_eh_valida(url):
        if url:
            return True
        else:
            return False

