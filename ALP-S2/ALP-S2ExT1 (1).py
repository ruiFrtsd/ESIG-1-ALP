from turtle import *
left(90)

def i_grc():
    #tronc
    forward(100)
    left(30)
    #branche gauche
    forward(100)
    back(100)
    #branche
    right(60)
    forward(100)
    back(100)
    left(30)
    back(100)

def double_i_grc():
    i_grc()
    back(100)
    left(60)
    i_grc()
    back(100)
    left(30)
    back(100)
    right(60)
    i_grc()

def quad_i_grc():
    #tronc
    i_grc()
    #deplacement vers branche gauche
    forward(100)
    left(30)
    forward(100)
    left(30)
    #dessine y  gauche
    i_grc()
    right(60)
    i_grc()
    #reviens au tronc
    left(30)
    back(100)
    right(60)
    
    
    forward(100)
    left(30)
    #dessine y  gauche
    i_grc()
    right(60)
    i_grc()
    
    
quad_i_grc()