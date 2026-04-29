import os 
from dataclasses import dataclass

os.system("cls")

#Definindo uma classe
@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

print("---Solicitando dados do Cliente---")
cliente = Cliente(
    nome = input("Digite o nome do cliente: "),
    email = input("Digite o e-mail do cliente: "),
    telefone = input("Digite o telefone do cliente: ")
)

print("\n---Dados do Cliente---")
print(f'Nome: {cliente.nome}')
print(f'E-mail: {cliente.email}')
print(f'Telefone: {cliente.telefone}')