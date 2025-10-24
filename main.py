lista = [0, 1]

def adicionar():
    adicao = lista[-1] + lista[-2]
    lista.append(adicao)

i = 0
while i < 10:
    adicionar()
    i += 1
    
input(lista)