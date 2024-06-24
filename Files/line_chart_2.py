from os import chdir
from pandas import read_excel
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from seaborn import *

# Dados
path = ('https://github.com/luizleal1974/GIF-Plot/blob/main/Files/airquality.xlsx')
dados = read_excel("airquality.xlsx")

# Grafico
fig, ax = plt.subplots()
set(style = "darkgrid", rc = {"lines.linewidth": 1}, palette = "pastel")
plt.subplots_adjust(left = 0.11, right = 0.76, top = 0.9, bottom = 0.2)

def animate(i):
    ax.clear()
    lineplot(x = dados.Dia[:i+1], y = dados.Temperatura, ax = ax, hue = dados.Mes)
    ax.set_xlim([min(dados.Dia), max(dados.Dia)])
    ax.set_ylim([min(dados.Temperatura), max(dados.Temperatura)])
    plt.title('Airquality', fontsize = 16)
    plt.legend(bbox_to_anchor = (1.05, 1), loc = 2, borderaxespad = 0.0, fontsize = '10').set_title("Mes")


# Save plot
chdir("F:") # set working directory
ani = FuncAnimation(fig, animate, frames = len(dados), repeat = True, repeat_delay = 0)    
ani.save("Line_Chart_Python_2.gif", dpi = 300, writer = PillowWriter(fps = 5))
