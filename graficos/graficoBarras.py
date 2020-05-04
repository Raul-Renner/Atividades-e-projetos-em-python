#Visualização em python

import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [9 ,5, 7, 3, 1]

x2 = [2, 4, 6, 8, 10]
y2 = [10 ,6, 8, 4, 2]

#Titulo
plt.title("Grafico de barras - 2")

#Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x1, y1, label = "Grupo 1")
plt.bar(x2, y2, label ="Grupo 2")

plt.legend()
plt.show()