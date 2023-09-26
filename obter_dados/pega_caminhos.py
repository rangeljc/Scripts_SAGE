# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:48:21 2023

@author: Julio Rangel
"""
import os

def pega_caminhos(arq, path = "./"):
    
    lista_de_caminhos = []
        
    for caminhos, pastas, arquivos in os.walk(path):
        if (arq in arquivos):
            caminho = (caminhos+"/"+arq).replace("\\", "/")
            lista_de_caminhos.append(caminho)
        
    if (lista_de_caminhos == []):
        print("Arquivo não encontrado na estrutura de pastas!")
    
    return lista_de_caminhos
    


if (__name__ == "__main__"):
    
    caminho = input("Entre com o caminho da pasta dados:\n")
    arquivo = input("Entre com o nome da entidade:\n")
    
    caminhos = pega_caminhos(arquivo, caminho)
    
    for i in caminhos:
        print(i)
    