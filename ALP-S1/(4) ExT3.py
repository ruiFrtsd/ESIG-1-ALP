from turtle import *
nPremier = int(input("Entrer nombre premier : "))
for i in range(4) :
    right(90)
    forward(nPremier) if i % 2 == 0 else forward(nPremier/2)    
    
# 
# right(90)
# forward(nPremier)
# right(90)
# forward(nPremier/2)
# right(90)
# forward(nPremier)
# right(90)
# forward(nPremier/2)