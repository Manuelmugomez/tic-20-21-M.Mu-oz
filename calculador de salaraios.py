def calcular_salario():
    num_horas = input("¿Cuantas horas ha trabajado esta semana?")
    salario=0
    if num_horas <=40:
        salario=num_horas*30
    else:
        horas_extras=num_horas-40
        salario=40*30+horas_extras*45
    print"el salario es de"+str(salario)

calcular_salario()
