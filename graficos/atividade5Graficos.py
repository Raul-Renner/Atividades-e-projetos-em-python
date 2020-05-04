import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

z = [200, 25, 400, 3300, 100]

titulo = "Graficos de Pontos"

eixox = "Eixo X"
eixoy = "Eixo y"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y, color = "#000000", linestyle = "-.")
plt.scatter(x, y, label = "Meus Pontos", color = "k",marker=".", s=z)
plt.legend()
#plt.show()
plt.savefig("arqPDF2.pdf", dpi=300)