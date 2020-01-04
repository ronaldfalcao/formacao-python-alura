from conta import Conta

# Permite rodar no terminal
if __name__ == '__main__':

    conta_a = Conta(1234, "Ronald", 5000.0, 10000.0)
    print(conta_a.limite)

    conta_b = conta_a  # Agora conta_a e conta_b apontam para o mesmo objeto

    conta_b.limite = 0  # Vai alterar o valor do limite na conta_a (conta_a.limite)

    print(conta_a.limite)
