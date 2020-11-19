def ejercicio_15():
    palabra=str(raw_input("dime una palabra"))
    primera_letra=list(palabra)[0]
    abc=["A","B","C","D","E"]
    for i in range(0,len(abc)):
        if abc[i]==primera_letra:
            print i+1


ejercicio_15()
