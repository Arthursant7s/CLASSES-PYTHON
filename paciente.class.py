import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float


print("---Solicitando dados do Paciente---")
paciente = Paciente(
    nome = input("Digite o nome do paciente: "),
    idade = int(input("Digite a idade do paciente: ")),
    peso = float(input("Digite o peso do paciente: ")),
    altura = float(input("Digite a altura do paciente: "))
)

print("\n---Dados do Paciente---")
print(f'Nome: {Paciente.nome}')
print(f'Idade: {Paciente.idade}')
print(f'Peso: {Paciente.peso}')
print(f'Altura: {Paciente.altura}')

# class Paciente:
#     def __init__(self, nome, idade, peso, altura):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.altura = altura

# print("---Solicitando dados do Paciente---")
# paciente = Paciente(
#         nome = input("Digite o nome do paciente: "),
#         idade = int(input("Digite a idade do paciente: ")),
#         peso = float(input("Digite o peso do paciente: ")), 
#         altura = float(input("Digite a altura do paciente: "))
#     )

# print("\n---Dados do Paciente---")
# print(f'Nome: {paciente.nome}')
# print(f'Idade: {paciente.idade}')
# print(f'Peso: {paciente.peso}')
# print(f'Altura: {paciente.altura}')

