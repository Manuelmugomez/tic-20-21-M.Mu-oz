def ejercicio_12():
    numero=str(input ("escriba un numero:"))
    lon = len(numero)
    suma = 0
    for cont in range(0, lon):
        suma = suma + int(numero[cont])
    print suma

    
ejercicio_12()
    
