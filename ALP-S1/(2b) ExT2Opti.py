from turtle import *
x = 60
right(30)
for i in range(4) :
    left(x) if i % 2 == 0 else left(x + x)
    forward(100)