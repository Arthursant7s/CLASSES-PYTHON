import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pessoa:
    nome: str
    idade: int


    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')

@dataclass
class Pet:
    nome: str
    idade: int

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')

# Usando uma classe
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

pet1 = Pet("Rex", 5)
pet2 = Pet("Mia", 3)

pessoa1.mostrar_dados()
pessoa2.mostrar_dados()
pet1.mostrar_dados()
pet2.mostrar_dados()