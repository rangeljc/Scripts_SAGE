import subprocess

comando = "Tabular -ent pas -atr id,valor".split()

saida= subprocess.run(comando, stdout = subprocess.PIPE)

resultado = str(saida.stdout).split("|")

resultado.pop(-1)
for i in range(10):
    resultado.pop(0)

dados = {"ID":[], "Valor":[]}

for i in range(0, len(resultado), 4): #resultado: #range(20):
    dados["ID"].append(resultado[i+2].strip())
    dados["Valor"].append(float(resultado[i+3].strip()))

for i in range(len(dados["ID"])):
    print("ID: {} = {}" .format(dados["ID"][i], dados["Valor"][i]))
