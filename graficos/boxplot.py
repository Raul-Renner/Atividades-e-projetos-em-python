import matplotlib.pyplot as plt
from random import randint

vetor = []

for i in range(6):
    numero_aleatorio = randint(0,10000)
    vetor.append(numero_aleatorio)
plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()