import subprocess

def pegar_medida(ponto):
    
    comando = ['Tabular -ent pas -atr valor -grep:id '+ponto]
    saida = subprocess.run(comando, stdout = subprocess.PIPE, shell = True)
    resultado = str(saida.stdout).split("|")
    #ponto = resultado[16].strip()
    resultado = float(resultado[15])
    
    print(resultado)

if (__name__ == "__main__"):

    ponto = input("Qual o ponto desejado: ").strip().upper()
    
    pegar_medida(ponto)