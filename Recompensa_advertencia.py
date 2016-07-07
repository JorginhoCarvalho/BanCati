# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:42:34 2016

@author: User
"""

class Advertencia:
    def __init__(self, Tipo, Data, Ponto, Justificativa, ID):
        self.Tipo = Tipo
        self.Data = Data
        self.Ponto = Ponto
        self.Justificativa = Justificativa 
        self.ID = ID
        
class Recompensa:
    def __init__(self, Coins, Data, Observacao, ID_Pessoa):
        self.Coins = Coins
        self.Data = Data
        self.Observacao = Observacao
        self.ID = ID_Pessoa