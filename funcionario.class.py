import os 
from dataclasses import dataclass

os.system("cls")

#Definindo uma classe
@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

@dataclass
class Funcionario:
    nome: str
    matricula: int
    email: str
    setor: str

    
funcionario1 = Funcionario('Zack', '28385', 'zack@gmail.com', 'ADM')

print("---Funcionário---")
print(f'Nome: {funcionario1.nome}')
print(f'Matrícula: {funcionario1.matricula}')
print(f'E-mail: {funcionario1.email}')
print(f'Setor: {funcionario1.setor}')
