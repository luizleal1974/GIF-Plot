library(animation)

# Data set
X = seq(from = -5, to = 5, by = 0.25)
Y = seq(from = -5, to = 5, by = 0.25)
R = function(x, y) sin(sqrt(x ^ 2 + y ^ 2))
Z = outer(X, Y, R)

# Surface
setwd("F:") # set working directory
saveGIF({
 for(i in 5:550){
     persp(x = X,
           y = Y,
           z = Z,
           main = expression(sin(sqrt(x^2+y^2))),
           cex.main = 2,
           cex.lab = 1.5,
           cex.axis = 1.5,
           theta = i,
           phi = 20,
           expand = 0.7,
           col = "lightblue",
           ltheta = 120,
           shade = 0.75,
           ticktype = "detailed")
 }
}, movie.name = "Surface_R.gif", interval = 0.05, ani.width = 480, ani.height = 480)