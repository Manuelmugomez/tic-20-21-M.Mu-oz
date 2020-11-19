# -*- coding: cp1252 -*-
def menu():
    interruptora=1
    print("Introduce dos numeros enteros")
    numero1=input("numero 1= ")
    while(interruptora==1):
        numero2=input("numero 2= ")
        print"*******************************************"
        print"*               MENU                      *"
        print"*******************************************"
        print"1. SUMA "
        print"2. RESTA "
        print"3. MULTIPLICACION "
        print"4. DIVISION "
        opcion=input ("Teclee la opcion elegida")
        if(opcion==1):
            resultado=numero1+numero2
            interruptora=0
        if(opcion==2):
            resultado=numero1-numero2
            interruptora=0
        if(opcion==3):
            resultado=numero1*numero2
            interruptora=0
        if(opcion==4):
            if(numero2<>0):
                resultado=numero1/numero2
                interruptora=0
            else:
                interruptora=1
                print("El valor 2 no es valido")
                print("introduce un valor nuevo para numero2")
    print"El resultado de la operacion es",resultado
    
menu()
    
