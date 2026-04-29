import os
from dataclasses import dataclass


os.system("cls")

@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass
class Pet:
    nome: str
    idade: int

    

    # Usando uma classe
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

pet1 = Pet("Rex", 5)
pet2 = Pet("Mia", 3)

print(f'Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\n')
print(f'Nome: {pet1.nome}\nIdade: {pet1.idade}\n')  
print(f'Nome: {pessoa2.nome}\nIdade: {pessoa2.idade}\n')
print(f'Nome: {pet2.nome}\nIdade: {pet2.idade}\n')

