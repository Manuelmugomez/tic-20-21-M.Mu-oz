def multiplicacion():
    acumuladora=1
    print"Introduce un numero:"
    for cont in range(0,5):
        print "numero",cont
        numero=input()
        acumuladora=acumuladora*numero
    print "producto:",acumuladora

multiplicacion()
