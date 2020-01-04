"""
Classe para formatar três valores passados como parâmetros no padrão dd/mm/yyyy.
"""


class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(f'{self.dia:02d}/{self.mes:02d}/{self.ano:04d}')
