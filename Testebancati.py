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

cursor.execute('''Drop table TesteBancati''')
cursor.execute('''create table TesteBancati( Nome text, Cargo text, Cati_coins integer, Login text, Senha text, ID integer)''')

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
        #Coins_total = resultado
        while resultado != None:
            print(resultado)
            resultado = cursor.fetchone()
            #Coins_total = resultado + Coins_total
    
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
            c = int(input("Quantos cati coins?"))
            cursor.execute('''Update TesteBancati set Cati_coins = ? where ID = ? ''',[c,Id_func])
            conn.commit() 
    
    def Unset_Cati_coins(self, Id_func):
            c = int(input("Quantos cati coins?"))
            cursor.execute('''Update TesteBancati set Cati_coins = ? where ID = ? ''',[c,Id_func])
            conn.commit() 
   
    def Reset_all(self):
            cursor.execute(''' Delete * from TesteBancati''')

#class Janela:
 #   def __init__(self, toplevel):
   #     self.fr1 = Frame(toplevel)
    #    self.fr1.pack()
        
     #   self.login = Label(self.fr1, text='Login:') 
      #  self.login.pack(side = LEFT) 
        
       # self.login_entry = Entry(self.fr1, bd = 5)
        #self.login_entry.pack(side = RIGHT)
        
        #self.senha = Label(self.fr1, text='Senha:') 
        #self.senha.pack(side = DOWN) 
        
       # self.senha_entry = Entry(self.fr1, bd = 5)
       # self.senha_entry.pack(side = DOWN)
        
#raiz = Tk()
    
#raiz.title("Bancati")
#raiz.geometry("400x300")'''



Iago = Administrador()
jorge = Pessoa('Jorge', 'Puto', 10, 'Jorge123', 'jorge123', 1234)
lucas = Funcionario('Lucas', 'Projetista', 15, 'lucas123', '123Lucas', 5431)

Iago.Cadastro('Marcelo', 'Desenvolvedor', 0 , 'Marcelo123', '123Marcelo', 9876)
Iago.Cadastro('Jorge', 'Puto', 10 , 'Jorge123', 'jorge123', 1234)
jorge.Exibir_Coins()
jorge.set_Login_Senha()

cursor.execute(''' Select * from TesteBancati''')
resultado = cursor.fetchone()
while resultado != None:
    print(resultado)
    resultado = cursor.fetchone()
            
cursor.close()
conn.commit()
conn.close()

#Janela(raiz)
#raiz.mainloop()     
    

