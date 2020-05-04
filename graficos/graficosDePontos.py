#Visualização em python

import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [9 ,5, 7, 3, 1]



#Titulo
plt.title("Graficos de dispersao - (Pontos)")


#Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

#plt.bar(x1, y1)
#plt.bar(x2, y2)
plt.plot(x1, y1, color = 'b', linestyle = '--')
plt.scatter(x1, y1, label = "Pontos", color = 'g', marker = "h", s = 100)
plt.legend()
plt.show()


"""
CORES (color)
'b' blue

'g' green

'r' red

'c' cyan

'm' magenta

'y' yellow

'k' black

'w' white



Marcadores (marker)
'.' point marker

',' pixel marker

'o' circle marker

'v' triangle_down marker

'^' triangle_up marker

'<' triangle_left marker

'>' triangle_right marker

'1' tri_down marker

'2' tri_up marker

'3' tri_left marker

'4' tri_right marker

's' square marker

'p' pentagon marker

'*' star marker

'h' hexagon1 marker

'H' hexagon2 marker

'+' plus marker

'x' x marker

'D' diamond marker

'd' thin_diamond marker

'|' vline marker

'_' hline marker





Tipos de linha (linestyle)
'-' solid line style

'--' dashed line style

'-.' dash-dot line style

':' dotted line style



Fonte: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
"""