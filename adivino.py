# -*- coding: cp1252 -*-
"""dime un nuemero al azar entre 1 y 10 y lo adivino"""
import random
def adivino():
    maxn=100
    numero=random.randint(1,maxn)
    intento=input("intentalo wacho: ")
    while intento!=numero:
        if intento>numero:
            print "tremenda tula te pasaste"
        if intento<numero:
            print"tremendo pilote de 3cm pero demasiado pequeño"
        intento=input("intentalo otra vez")

    print "Asertaste wuacho"


adivino()
