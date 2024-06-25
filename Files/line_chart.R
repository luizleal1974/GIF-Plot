library(plotly)
library(xlsx)
library(gganimate)

# Dados
arquivo = tempfile(fileext = ".xlsx")
path = "https://github.com/luizleal1974/GIF-Plot/raw/main/Files/airquality.xlsx"
download.file(path, destfile = arquivo, mode = 'wb')
dados = read.xlsx(arquivo, sheetIndex = 1, encoding = "UTF-8")

# Ordenar string
dados$Mes = factor(dados$Mes, levels = c("Maio", "Junho", "Julho", "Agosto", "Setembro"))

# Grafico
ggplot(data = dados, mapping = aes(x = Dia, y = Temperatura, color = Mes)) +
geom_line(linewidth = 1) +
labs(title = "Airquality") +
theme(plot.title   = element_text(color = "black", size = 20, angle = 0 , hjust = 0.5, vjust = 0.5, face = "plain"),
      axis.text.x  = element_text(color = "black", size = 20, angle = 0 , hjust = 0.5, vjust = 0.5, face = "plain"),
      axis.text.y  = element_text(color = "black", size = 20, angle = 0 , hjust = 0.5, vjust = 0.5, face = "plain"),
      axis.title.x = element_text(color = "black", size = 20, angle = 0 , hjust = 0.5, vjust = 0.5, face = "plain"),
      axis.title.y = element_text(color = "black", size = 20, angle = 90, hjust = 0.5, vjust = 0.5, face = "plain"),
      legend.title = element_text(size = 20),
      legend.text  = element_text(size = 20),
      plot.margin  = margin(t = 10, r = 0, b = 10, l = 10)
) +
transition_reveal(Dia)