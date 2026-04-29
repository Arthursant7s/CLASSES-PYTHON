import os 
from dataclasses import dataclass

os.system("cls")

#Definindo uma classe
@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'Telefone: {self.telefone}')

print("---Solicitando dados do Cliente---")
cliente = Cliente(
    nome = input("Digite o nome do cliente: "),
    email = input("Digite o e-mail do cliente: "),
    telefone = input("Digite o telefone do cliente: ")
)

print("\n---Dados do Cliente---")
cliente.mostrar_dados()