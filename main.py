import media;
import aleatorio;
from statistics import *
lista = aleatorio.gerarLista(5)
print(lista)

'''
print("moda: " , mode(lista))
print("media: ",mean(lista))
print("mediano:",median(lista))
'''

result = media.media(lista)
print("media da lista é: ",result)

result2 = media.mediana(lista)
print("mediana da lista é: ", result2)

result = media.moda(lista)
print("moda da lista é: ", result)