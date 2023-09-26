# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:44:40 2023

@author: Julio Rangel
"""
from pega_caminhos import pega_caminhos
from le_dat import le_dat
from encontra_dats import encontra_dats

def start(caminho = "./"):
    
    path = caminho.replace("\\", "/")
    arquivos = encontra_dats(path)
    
    for arquivo in arquivos:
        caminhos = pega_caminhos(arquivo, path)
        le_dat(arquivo, caminhos)
    
    print('Processo de Obtenção de dados encerrado!')



if (__name__ == "__main__"):
    
    caminho = input("Entre com o caminho da pasta dados:\n")
    
    start(caminho)