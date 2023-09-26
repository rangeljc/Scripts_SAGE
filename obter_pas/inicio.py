import obter_pas as pas

def start():
    path = input("Forneca o endereco completo do arquivo pas:\n")
    pas.obter_pas(path)

if (__name__ == "__main__"):
    start()