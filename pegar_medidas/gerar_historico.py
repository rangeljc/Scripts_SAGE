import subprocess
from datetime import datetime, timedelta

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
        print("Opa, algo de errado com o formato das datas ou horas..")
        print("Por favor, insira data no formato dd/mm/aaaa")
        print("e hora no formato hh:mm")
        data = datetime.now()
    
    except ValueError:
        print("Opa, algo de errado com o formato das datas ou horas..")
        print("Por favor, insira data no formato dd/mm/aaaa")
        print("e hora no formato hh:mm")
        data = datetime.now()
        
    except Exception as erro:
        print(type(erro), erro)
      
    finally:
        return data
    

def gerar_historico_pas(ponto, data_inicio, hora_inicio, data_fim, hora_fim):
    
    # ajuste das variaveis auxiliares
    while (not ponto):
        print("O ID do ponto é necessário para a busca...")
        ponto = input("Qual o ponto desejado: ").strip().upper()
        
    meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
    
    inicio = manipula_data(data_inicio, hora_inicio)
    fim = manipula_data(data_fim, hora_fim)
        
    dia_anterior = 0
    
    while (inicio <= fim):
        
        if (inicio.day != dia_anterior):
            mes = meses[inicio.month-1]
            dia = inicio.strftime("%d")
            ano = inicio.strftime("%y")
            
            caminho = "/var/sage/arqs/"+mes+dia+ano+".pas"    
        
            # rotina para encontrar o indice do ponto dentro do aquivo pas
            comando = ['grep -n ' + ponto + ' ' + caminho]            
            try:
                indice_ponto = int(executa_comando(comando).split(":")[0].split("'")[1])-2
                ponto_existe = True
                
            except ValueError:
                print("Ponto inválido ou não encontrado no histórico do dia {}!" .format(inicio.strftime("%d/%m/%y")))
                ponto_existe = False
        
        dia_anterior = inicio.day
        
        if (ponto_existe):
            horario = str(inicio.strftime("%H:%M:%S"))
            
            # rotina para encontrar o indice da hora desejada
            comando = ['grep -n ' + horario + ' ' + caminho + ' | tail -1']
            indice_hora = int(executa_comando(comando).split(":")[0].split("'")[1])
            
        
            # rotina para encontrar o valor desejado
            comando = ['head -n ' + str(indice_hora+indice_ponto) +' '+ str(caminho) + ' | tail -1']
            valor = float(executa_comando(comando).split("\\n")[0].split("'")[1].strip().replace("*","0"))
        
            print("{} {}: {}" .format(inicio, ponto, valor))
        
            inicio = inicio + timedelta(minutes = 5)
        
        else:
            inicio = inicio + timedelta(days = 1)
            inicio = manipula_data(inicio.strftime("%d/%m/%Y"), "00:00")
            
        

if (__name__ == "__main__"):
   
    print("**----------------------------------------------------------**")
    print("** ATENÇÃO! Insira as informações nos formatos indicados!   **")
    print("** Caso as informações de data e hora não sejam informados, **")
    print("** o resultado será o último registro cadastrado.           **")
    print("** O ID do ponto é entrada obrigatória!                     **")
    print("**----------------------------------------------------------**")
    
    ponto = input("Qual o ponto desejado: ").strip().upper()
    data_inicio = input("Data inicial desejada (dd/mm/aaaa): ").strip()
    hora_inicio = input("Hora inicial desejada (hh:mm): ")
    data_final = input("Data Final desejada (dd/mm/aaaa): ").strip()
    hora_final = input("Hora Final desejada (hh:mm): ")

    gerar_historico_pas(ponto, data_inicio, hora_inicio, data_final, hora_final)
