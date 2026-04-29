import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Peso: {self.peso}')
        print(f'Altura: {self.altura}')
    

print("---Solicitando dados do Paciente---")
paciente = Paciente(
    nome = input("Digite o nome do paciente: "),
    idade = int(input("Digite a idade do paciente: ")),
    peso = float(input("Digite o peso do paciente: ")),
    altura = float(input("Digite a altura do paciente: "))
)

print("\n---Dados do Paciente---")
paciente.mostrar_dados()

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

