from datetime import datetime, timedelta


class DatasBr:

    def __init__(self):
        self.data_cadastro = datetime.now()

    def __str__(self):
        return self.data_hora_formatada()

    def retorna_semana_cadastro(self):

        dias_semana = [
                        'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira',
                        'sexta-feira', 'sábado', 'domingo'

                      ]

        return dias_semana[self.data_cadastro.weekday()]

    def retorna_mes_cadastro(self):

        meses = [
                    'janeiro', 'fevereiro', 'março', 'abril',
                    'maio', 'junho', 'julho', 'agosto', 'setembro',
                    'outubro', 'novembro', 'dezembro'
                 ]

        return meses[self.data_cadastro.month - 1]

    def data_formatada(self):
        return self.data_cadastro.strftime("%d/%m/%Y")

    def hora_formatada(self):
        return self.data_cadastro.strftime("%H:%M:%S")

    def data_hora_formatada(self):
        return self.data_cadastro.strftime("%d/%m/%Y - %H:%M:%S")

    def define_prazo_expiracao(self):
        return self.data_cadastro + timedelta(days=15)
