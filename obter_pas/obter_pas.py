import pandas as pd

def obter_pas(arquivo_pas):
    with open(arquivo_pas, "r") as arquivo:
        index = 0
        medidas_total = {"Pontos PAS" : []}
        for linha in arquivo.readlines():
            informacao = linha.strip().split()
            if (index == 0):
                dados = {"Dia da Semana": informacao[0],
                        "Dia": informacao[2],
                        "Mes": informacao[1],
                        "Ano": informacao[4],
                        "Horario Inicial": informacao[3]}
            elif (index == 1):
                dados["Quantidade de Pontos"] = int(informacao[1])
            else:
                if (len(informacao) == 1):
                    informacao = str(informacao[0]).replace("*", "0")
                    try:
                        medidas_total[horario].append(float(informacao))
                    
                    except NameError:
                        medidas_total["Pontos PAS"].append(informacao)
                    
                else:
                    horario = informacao[1]
                    medidas_total[horario] = []
                    
            index +=1
    
    dados["Horario Final"] = horario
    nome_arquivo_saida = dados["Mes"]+dados["Dia"]+dados["Ano"]+"_"+str(dados["Quantidade de Pontos"])+"pas"
    planilha = pd.DataFrame(medidas_total)
    cabecalho = pd.DataFrame(dados, index=["1"])
    planilha.to_csv(nome_arquivo_saida+'.csv', index=False)
    with pd.ExcelWriter(nome_arquivo_saida+'.xlsx') as writer:  
        cabecalho.to_excel(writer, sheet_name='Cabeçalho', index = False)
        planilha.to_excel(writer, sheet_name='Pontos PAS', index = False)


if (__name__ == "__main__"):
    path = input("Forneca o endereco completo do arquivo pas:\n")
    obter_pas(path)
