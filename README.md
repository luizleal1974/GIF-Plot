# GIF Plot

<p align="justify">GIF significa <i>Graphics Interchange Format</i> (Formato de Intercâmbio Gráfico). Este repositório fornece códigos de programação em R e Python para salvar gráficos em formato GIF.</p>
  
</br>

# Surface

Os arquivos <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/Surface.R'><code>Surface.R</code></a> e <a target='_blank' rel='noopener noreferrer' href='https://github.com/luizleal1974/GIF-Plot/blob/main/Files/Surface.py'><code>Surface.py</code></a> contém sugestões de códigos para a construção de gráficos 3D.

```{r}
# Run this code in R prompt
# Surface
path1 = "https://github.com/luizleal1974/GIF-Plot/raw/main/Files/Surface.R"
path2 = "https://github.com/luizleal1974/GIF-Plot/raw/main/Files/Surface.py"
p1 = devtools::source_url(path1)
p2 = reticulate::source_python(path2)
p1 ; p2
```


<table width="100%">
<tr>
<td><p align="center"><img src="/Files/Surface_R.gif" height="300" width="300" alt="Drawing"/></p><p align="center">(a)</p></td>
<td><p align="center"><img src="/Files/Surface_Python.gif" height="300" width="450" alt="Drawing"/></p><p align="center">(b)</p></td>
</tr>
</table>

<div align="center">Figura 1. Gráfico 3D: (a) R; (b) Python.</div>
