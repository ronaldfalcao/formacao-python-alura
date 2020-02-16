from cpf import Cpf
from cnpj import Cnpj

# Utilizando a classe CPF criada.
cpf = Cpf(71541456092)
print(cpf.formatar_cpf())
print(cpf)

""" Erro
cpf_menor = Cpf(345678912)
print(cpf_menor.formatar_cpf())
print(cpf_menor)
"""

# Utilizando a classe CNPJ criada
print("\nCriando CNPJ")
cnpj = Cnpj("18737414000163")
print(cnpj.formatar_cnpj())
print(cnpj)


"""
Criar a classe cpf_cnpj com o parâmetro tipo_documento (cpf ou cnpj) no construtor
Criar a classe cnpj
Criar esquema de factory Factory(classe Documento), DocCpf e DocCnpj)

"""


