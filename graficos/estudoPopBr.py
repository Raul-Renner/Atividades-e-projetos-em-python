
import matplotlib.pyplot as plt

dados = open("projeto/original.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

#Grafico de barras
plt.bar(x, y, color="#e4e4e4")

#funcao da criacao do grafico de linha
plt.plot(x, y, color = "k", linestyle = ":")

plt.title("Crescimento da População Brasileira 1980 - 2015")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")

#mostrar grafico
#plt.show()

plt.savefig("populacao_brasileira_.pdf",dpi = 300)