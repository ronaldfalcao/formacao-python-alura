from cpf import Cpf
from cnpj import Cnpj
from cpf_cnpj import CpfCnpj


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

# Utilizando a classe CpfCnpj
print("\nCriando CPF")
documento = CpfCnpj.criar_novo_documento("18353600099", 'cpf')
print(documento)

print("\nCriando CNPJ")
documento = CpfCnpj.criar_novo_documento("45066477000108", 'cnpj')
print(documento)


"""
Criar esquema de factory Factory(classe Documento), DocCpf e DocCnpj)

"""


