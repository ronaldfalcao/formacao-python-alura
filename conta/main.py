from conta import Conta

# Permite rodar no terminal
if __name__ == '__main__':

    conta = Conta(1234, "Ronald", 5000.0, 10000.0)

    conta.depositar(1000)
    conta.exibir_extrato()

    conta.sacar(2000)
    conta.exibir_extrato()
