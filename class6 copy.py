import os
from dataclasses import dataclass

os.system("cls")


@dataclass
class Fornecedor:
    nome: str
    email: str
    telefone: str
    Endereço: str


    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'Telefone: {self.telefone}')
        print(f'Endereço: {self.Endereço}')



print("---Solicitando dados do Fornecedor---")
fornecedor = Fornecedor(
    nome = input("Digite o nome do fornecedor: "),
    email = input("Digite o e-mail do fornecedor: "),
    telefone = input("Digite o telefone do fornecedor: "),
    Endereço = input("Digite o endereço do fornecedor: ")
)

print("-------------------------------------------")

print("\n---Dados do Fornecedor---")
fornecedor.mostrar_dados()
