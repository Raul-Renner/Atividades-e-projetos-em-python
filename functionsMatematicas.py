teste = 0
def media(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    media = soma / len(lista)
    return media
def mediana(lista):
    mediana = 0
    lista_ordenada = sorted(lista)
    tam = len(lista_ordenada)
    if(tam % 2 == 0):
        mediana = (lista_ordenada[int(tam/2)] + lista_ordenada[int (tam/2) - 1]) / 2
    elif(tam % 2 == 1):
        mediana = lista_ordenada[int (tam/2)]
    return mediana

def moda(lista):
    lista_dicionario = {}

    for l in lista:
        if l not in lista_dicionario:
            lista_dicionario[l] = 1
        else:
            lista_dicionario[l] += 1
    max_repeticao = max(lista_dicionario.values())
    for i in lista_dicionario:
        if lista_dicionario[i] == max_repeticao:
            moda = i
    return moda        