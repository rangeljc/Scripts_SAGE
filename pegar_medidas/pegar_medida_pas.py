import subprocess
from datetime import datetime

def executa_comando(comando):
    
    saida = subprocess.run(comando, stdout = subprocess.PIPE, shell = True)
    
    return str(saida.stdout)

def manipula_data(dt, hr):
    
    if (not dt):
        dt = datetime.now().strftime("%d/%m/%Y")
    
    if (not hr):
        hr = datetime.now().strftime("%H:%M")
    
    s = ".-"
    for i in range(len(s)):
        dt = dt.replace(s[i], "/")
        hr = hr.replace(s[i], ":")
        
    dt = dt.split("/")
    hr = hr.split(":")
    
    try:    
        data = datetime(
            int(dt[2].strip()),
            int(dt[1].strip()),
            int(dt[0].strip()),
            int(hr[0].strip()),
            int(int(hr[1].strip())/5)*5, 0)
    
    except IndexError:
        data = False
    
    except ValueError:
        data = False
        
    except Exception as erro:
        print(type(erro), erro)
      
    finally:
        return data

def pegar_medida_pas(pto, dt, hr):
    
    while (not pto):
        print("O ID do ponto desejado é obrigatório!")
        pto = input("Qual o ponto desejado: ").strip().upper()
        
    meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
    
    data = manipula_data(dt, hr)
    
    if (data):
        
        dia = data.strftime("%d")
        mes = meses[data.month-1]
        ano = data.strftime("%y")
        horario = data.strftime("%H:%M:%S")
        
        caminho = "/var/sage/arqs/"+mes+dia+ano+".pas"
        
        comando = ['grep -n ' + pto + ' ' + caminho]
        try:
            indice_ponto = int(executa_comando(comando).split(":")[0].split("'")[1])-2
            ponto_existe = True
        
        except ValueError:
            print("Ponto inválido ou não encontrado no histórico do dia {}!" .format(data.strftime("%d/%m/%y")))
            ponto_existe = False
    
        if (ponto_existe):
            comando = ['grep -n ' + horario + ' ' + caminho]
            indice_hora = int(executa_comando(comando).split(":")[0].split("'")[1])
        
            comando = ['head -n ' + str(indice_hora+indice_ponto) + ' ' + caminho + ' | tail -1']
            valor = float(executa_comando(comando).split("\\n")[0].split("'")[1].strip())
        
            print("{} --> {}: {}" .format(data, pto, valor))
    
    else:
        print("Opa, algo de errado com o formato das datas ou horas..")
        print("Por favor, insira data no formato dd/mm/aaaa")
        print("e hora no formato hh:mm")

if (__name__ == "__main__"):

    ponto = input("Qual o ponto desejado: ").strip().upper()
    data = input("Data desejada(dd/mm/aa): ").strip()
    hora = input("qual a hora desejada (hh:mm): ").strip()

    pegar_medida_pas(ponto, data, hora)
