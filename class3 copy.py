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


    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Matrícula: {self.matricula}')
        print(f'E-mail: {self.email}')
        print(f'Setor: {self.setor}')

    
funcionario1 = Funcionario('Zack', '28385', 'zack@gmail.com', 'ADM')

print("---Funcionário---")
funcionario1.mostrar_dados()
