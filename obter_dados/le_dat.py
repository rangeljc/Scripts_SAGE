# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 07:49:25 2023

@author: Julio Rangel
"""

import pandas as pd


def le_dat(arq, caminhos = ["./"]):
    
    dados = {}
    nome_planilha = arq.split(".")[0]
    
    for caminho in caminhos:
        with open(caminho, "r") as arquivo:
            indice_linha = 1
            
            include = caminho.split("/dados/")[1]
            if (include == arq):
                include = "dados/"
            else:
                include = include.split(arq)[0]
            
            for linha in arquivo.readlines():
                informacao = linha.strip()
                if (informacao == ""):
                    pass
                
                elif ("#include" in informacao): #linhas de include
                    pass
                
                elif (informacao[0] == ";"): #linhas de comentarios
                    pass
                
                elif ("=" in informacao): #linhas com os dados das entidades
                    
                    informacao = informacao.split("=")
                    
                    campo = informacao[0].strip()
                    if (len(informacao) > 2):
                        valor = informacao[1].strip()
                        for i in range(len(informacao)-2):
                            valor = "=".join([valor, informacao[i+2].strip()])
                    else:
                        valor = informacao[1].strip()
                    
                    if (campo in dados.keys()):
                        dados[campo].append(valor)
                    
                    else:
                        dados[campo] = []
                        for i in range(len(dados[campo_inicial])-1):
                            dados[campo].append("")
                        dados[campo].append(valor)
                           
                else: #linhas com o nome da entidade
                    if (not dados):
                        dados["INCLUDE"] = []
                        dados["INCLUDE"].append(include)
                        campo_inicial = "INCLUDE"
                    else:
                        dados["INCLUDE"].append(include)
                
                indice_linha += 1
            
           
        
        for chave in dados.keys():
            teste = len(dados[campo_inicial]) - len(dados[chave])
            if (teste > 0):
                for i in range(teste):
                    dados[chave].append("")
        
    planilha = pd.DataFrame(dados)
    
    with pd.ExcelWriter(nome_planilha+".xlsx") as writer:  
        planilha.to_excel(writer, sheet_name = nome_planilha, index = False)


if (__name__ == "__main__"):
    caminho = []
    caminho.append(input("Entre com o caminho da entidade desejada:\n"))
    le_dat(caminho)