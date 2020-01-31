import os 

def Inputs(path,tipoDoId,campoASerCriado):
    campoASerCriado = input('Nome do Campo a ser criado')
    tipoDoId = input('Tipo do ID a ser criado')
    path = "C:/SoftplanDirProject/" + campoASerCriado
    return path,tipoDoId,campoASerCriado