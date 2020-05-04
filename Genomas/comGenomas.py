entrada = open("projeto/16s_bacteria.fasta").read()
saida = open("projeto/bacteria.html","w")

cont = {}
seqADN = ['A','T','C','G'];
for i in seqADN:
    for j in seqADN:
        cont[i + j] = 0

entrada = entrada.replace("\n","")
for k in range(len(entrada) - 1):
    cont[entrada[k] + entrada[k + 1]] += 1


saida.write("<div>")
i = 1
for k in cont:
    transparencia = cont[k] / max(cont.values())
    saida.write("<div style = 'Width: 100px; border: 1px solid #111; color:#ffff; height:100px; float:left;background-color:rgba(0, 0, 0, "+ str(transparencia)+"')>"+k+"</div>")

    if i % 4 == 0:
        saida.write("<div style='clear:both'></div>")
    i += 1
saida.close()
