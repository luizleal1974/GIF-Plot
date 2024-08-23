# 1. GIF Plot

<p align="justify">GIF significa <i>Graphics Interchange Format</i> (Formato de Intercâmbio Gráfico). Este repositório fornece códigos de programação em R e Python para salvar gráficos em formato GIF.</p>

<p align="justify"><b>É importante destacar que no Python faz-se necessário instalar o módulo  PIL (Python Imaging Library): <code>pip install pillow</code>.</b></p>

```{r}
# Run this code in R prompt
library(reticulate)
py_install("pillow")
```

</br>





# 2. Superfície

<p align="justify">Os arquivos <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/Surface.R'><code>Surface.R</code></a> (pacote <code><b>animation</b></code>) e <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/Surface.py'><code>Surface.py</code></a> contém sugestões de códigos para a construção de gráficos de superfície.</p>

<p align="center"><img src="/Files/Surface.gif" alt="Drawing"/></p>

<div align="center">Figura 1. Gráfico 3D: (a) <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/Surface.R'><code>Surface.R</code></a>; (b) <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/Surface.py'><code>Surface.py</code></a>.</div>

</br>





# 3. Gráfico de linhas

<p align="justify">Os arquivos <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/line_chart.R'><code>line_chart.R</code></a> (pacote <code><b>gganimate</b></code>), <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/line_chart_1.py'><code>line_chart_1.py</code></a> e <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/line_chart_2.py'><code>line_chart_2.py</code></a> contém sugestões de códigos para a construção de gráficos de linha.</p>
  
<p align="justify">No que tange a linguagem de programação R, há um vídeo tutorial disponível no <a target='_blank' rel='noopener noreferrer' href='https://www.youtube.com/watch?v=CUZJTCrZiys&list=PL9QQDIVZa2ab9B2rieO41mLV2xFnsA70e&index=3&t=37s'><code><b>YouTube</b></code></a> que apresenta um modo alternativo para salvar gráficos em formato GIF.</p>

<p align="center"><img src="/Files/line_chart.gif" alt="Drawing"/></p>

<div align="center">Figura 2. Gráfico de linhas: (a) <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/line_chart.R'><code>line_chart.R</code></a>; (b) <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/line_chart_1.py'><code>line_chart_1.py</code></a>; (c) <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/line_chart_2.py'><code>line_chart_2.py</code></a>.</div>

</br>




# 4. Scatter plot 3D

### 4.1 Introdução

<p align="justify">Os arquivos <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/scatter_plot_3D.R'><code>scatter_plot_3D.R</code></a> (pacote <code><b>gifski</b></code>) e <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/scatter_plot_3D.py'><code>scatter_plot_3D.py</code></a> contém sugestões de códigos para a construção de scatter plot 3D.</p>

<p align="center"><img src="/Files/scatter_plot_3D.gif" alt="Drawing"/></p>

<div align="center">Figura 3. Scatter plot 3D: (a) <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/scatter_plot_3D.R'><code>scatter_plot_3D.R</code></a>; (b) e (c) <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/scatter_plot_3D.py'><code>scatter_plot_3D.py</code></a>.</div>

</br>

### 4.2 Python

<p align="justify">No <a target='_blank' rel='noopener noreferrer' href='https://colab.research.google.com/drive/1O-b1gdbIZh6J43sdvwWSFowY9KSj2gyu?usp=sharing'><code>Google Colab</code></a> há o código de programação em Pyhton <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/scatter_plot_3D_Python_3.py'><code>scatter_plot_3D_Python_3.py</code></a> para construção da figura 4. Para informações complementares acesse <a target='_blank' rel='noopener noreferrer' href='https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html'><code>mplot3d View Angles</code>.</p>

<p align="center"><img src="/Files/scatter_plot_3D_Python_3.gif" alt="Drawing"/></p>

<div align="center">Figura 4. Scatter plot 3D no Python: <code>ax.view_init(roll = i)</code>.</div>

</br>




# 5. Vídeo (MP4)

Os arquivos <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/line_chart.R'><code>line_chart.R</code></a> e <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/line_chart_1.py'><code>line_chart_1.py</code></a> contém códigos de programação para salvar gráficos em formato de vídeo com extensão MP4. Para fazer download dos vídeos clique em <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/Video_MP4.zip'><code><b>Video_MP4.zip</b></code></a>.


<p align="center"><img src="/Files/Video_MP4.gif" alt="Drawing"/></p>

<div align="center">Figura 5. Vídeo (MP4): <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/Video_MP4.zip'><code><b>Video_MP4.zip</b></code></a>.</div>

</br>






