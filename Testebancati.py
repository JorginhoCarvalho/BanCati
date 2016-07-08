# -*- coding: utf-8 -*-
#from tkinter import *
import sqlite3
from Recompensa_advertencia import *


conn = sqlite3.connect('testeBancati.bd')
cursor = conn.cursor()
"""
Created on Wed Jul  6 10:19:57 2016

@author: Jorge e Atletica
"""

"""cursor.execute('''Drop table if exists TesteBancati ''')
cursor.execute('''Drop table if exists Advertencia ''')
cursor.execute('''Drop table if exists Recompensa ''')"""
cursor.execute('''create table if not exists TesteBancati( Nome text, Cargo text, Cati_coins integer, Login text, Senha text, ID integer)''')
cursor.execute('''create table if not exists Advertencia( Tipo text, Data text, Ponto integer, Justificativa text, ID_Func integer)''')
cursor.execute('''create table if not exists Recompensa( Coins integer, Data text, Observacao text, ID_Func integer)''')

class Pessoa:    
    
    def __init__(self, Nome, Cargo, Cati_coins, Login, Senha, ID):
        self.Cati_coins = Cati_coins
        self.Cargo = Cargo
        self.Nome = Nome
        self.Login = Login
        self.Senha = Senha
        self.ID = ID
        
    def Exibir_Coins(self):
        cursor.execute('''Select Cati_coins from TesteBancati where ID = ?''', [self.ID])
        resultado = cursor.fetchone()
        print(resultado)                    
    
    def Get_Id(self):
        return self.ID
    
    def set_Login_Senha(self):
        Login = input("Login:")
        Senha = input("Senha:")
        self.Login = Login
        self.Senha = Senha
        cursor.execute(''' update TesteBancati set Login = ? where ID = ?''', [self.Login, self.ID])
        conn.commit()        
        cursor.execute(''' update TesteBancati set Senha = ? where ID = ?''', [self.Senha, self.ID])
        conn.commit()
    
class Funcionario(Pessoa):
    pass

class Administrador():
    def __init__(self):
        pass
        
    def Cadastro(self, Nome, Cargo, Cati_coins, Login, Senha, ID):
        cursor.execute('''insert into Testebancati values(?,?,?,?,?,?)''',
                       [Nome, Cargo, Cati_coins, Login, Senha, ID])
    
    def Set_Cati_coins(self, Id_func):
            c = int(input("Quantos cati coins? "))
            cursor.execute('''Update TesteBancati set Cati_coins = Cati_coins + ? where ID = ? ''',[c,Id_func])
            conn.commit() 
    
    def Unset_Cati_coins(self, Id_func):
            c = int(input("Quantos cati coins? "))
            cursor.execute('''Update TesteBancati set Cati_coins = Cati_coins - ? where ID = ? ''',[c,Id_func])
            conn.commit() 
   
    def Cadastrar_Advertencia(self, Tipo, Data, Ponto, Justificativa):
            '''Soh instanciei essa classe para mostrar que o import esta dando certo'''
            fodeu = Advertencia(Tipo, Data, Ponto, Justificativa)
            cursor.execute(''' insert into Advertencia values(?,?,?,?,?)''',[Tipo, Data, Ponto, Justificativa, Id_func])
    
    def Cadastrar_Recompensa(self, Coins, Data, Observacao, Id_func):
            '''Soh instanciei essa classe para mostrar que o import esta dando certo'''
            boa = Recompensa(Ponto, Data, Observacao, Id_func)            
            cursor.execute(''' insert into Recompensa values(?,?,?,?,?)''',[Coins, Data, Observacao, Id_func])    
    
    def Reset_all(self):
            cursor.execute(''' Delete * from TesteBancati''')
            cursor.execute(''' Delete * from Advertencia''')
            cursor.execute(''' Delete * from Recompensa''')

Iago = Administrador()
jorge = Pessoa('Jorge', 'Maneh', 10, 'Jorge123', '123Jorge', 1234)
lucas = Funcionario('Lucas', 'Projetista', 15, 'lucas123', '123Lucas', 5431)

Iago.Cadastro('Marcelo', 'Desenvolvedor', 0 , 'Marcelo123', '123Marcelo', 9876)
Iago.Cadastro('Jorge', 'Puto', 10 , 'Jorge123', 'jorge123', 1234)

Iago.Set_Cati_coins(jorge.Get_Id())

cursor.execute(''' Select Distinct * from TesteBancati''')
resultado = cursor.fetchone()
while resultado != None:
    print(resultado)
    resultado = cursor.fetchone()
            
cursor.close()
conn.commit()
conn.close()


