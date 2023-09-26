import subprocess

def pegar_estados(ponto):
    
    while (not ponto):
        print("O ID do ponto é obrigatório!\n")
        ponto = input("Qual o ponto desejado: ").strip().upper()
    
    comando = ['Tabular -ent pds -atr a1_flags -grep:id ' + ponto + ' | tail -2 | head -1']
    saida = subprocess.run(comando, stdout = subprocess.PIPE, shell = True)
    resultado = str(saida.stdout).split("|")
    
    try:
        ponto = resultado[4].strip()
        flags = resultado[3].strip().split()
        
        estado = "Atuado" if (flags[3][7] == "1") else "Desatuado"
    
        print(ponto, estado)
        
    except IndexError:
        print("Ponto inválido ou não encontrado!")
    

if (__name__ == "__main__"):

    ponto = input("Qual o ponto desejado: ").strip().upper()
    
    pegar_estados(ponto)