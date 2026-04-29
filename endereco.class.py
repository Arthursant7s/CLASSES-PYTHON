import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: str

# Definindo uma classe
@dataclass
class Cliente:
    nome: str
    idade: int
    endereco: Endereco

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Endereço: {self.endereco.logradouro}')
        print(f'Número: {self.endereco.numero}')

print("---Solicitando dados do Endereço---")
Cliente = Cliente(
    nome = input("Digite o nome: "),
    idade = int(input("Digite a idade: ")),
    endereco = Endereco(
        logradouro = input("Digite o logradouro: "),
        numero = input("Digite o número: ")
    )
)

print("\n---Dados do Endereço---")
Cliente.mostrar_dados()