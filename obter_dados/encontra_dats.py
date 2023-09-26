# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 10:16:46 2023

@author: Julio Rangel
"""
import os

def encontra_dats(caminho = "./"):
    
    lista_dats = []
    for _, _, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            if ((".dat" in arquivo) and (arquivo not in lista_dats)):
                lista_dats.append(arquivo)
    
    #print(lista_dats, len(lista_dats))
    
    return lista_dats

if (__name__ == "__main__"):
    
    caminho = input("Entre com o caminho da pasta dados:\n")
    dat_files = encontra_dats(caminho)
    
    for dat in dat_files:
        print(dat)
    
    print('Encontrados ' + len(dat_files) + ' arquivos!')