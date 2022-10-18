import random #Importar funcion que tira un valor aleatorio
nom=input("Ingresar nombre: \n") #Nombre del jugador

def modofacil():
    x=random.randint(1, 20) #Variable con la funcion random, que tira un valor aleatorio de tipo entero
    cont=0 #contador para el for
    for n in range(12):    
        num=input("Ingresar un número, e intentar acertar el número aleatorio o ingresar x para salir: \n")
        print("")

        while not num.isnumeric() and num != "x".lower() or int(num)>20:        
            num=input("Ingresar variables numéricas, e intentar acertar el número aleatorio: \n")
            print("")

        if num == "X".lower(): #Si el valor es el string "x", rompe el for
            break

        if int(num)==x: #Si num es de tipo entero y su valor es igual que el de x, ganas la partida
            print (f"Usted acertó, el número era: {x}. \nUsted, {nom}, ha ganado!\n")
            break
        elif int(num)>x: #Si no seguis jugando, con menos intentos. En este caso muestra si el valor ingresado es mayor o menor
            cont=cont+1
            print ("Valor incorrecto, el número ingresado es mayor al número a adivinar. \nLe quedan",10-cont,"Oportunidades.\n")     
        else:
            cont=cont+1
            print ("Valor incorrecto, el número ingresado es menor al número a adivinar. \nLe quedan",10-cont,"Oportunidades.\n")
            
        if cont == 10:
            print("Intentarlo en otra ocasión. GAME OVER PAPÁ. \n")
            break

def mododificil(): #Aca el codigo es igual, pero sin la parte de mostrar si el valor ingresado es mayor o menor que el valor de x
    x=random.randint(1, 20)

    cont=0

    for n in range(12):    
        num=input("Ingresar un número, e intentar acertar el número aleatorio o ingresar x para salir: \n")
        print("")
        while not num.isnumeric() and num != "x".lower() or int(num)>20:        
            num=input("Ingresar variables numéricas, e intentar acertar el número aleatorio: \n")
            print("")
        if num == "X".lower():
            break

        if int(num)==x:
            print (f"Usted acertó, el número era: {x}. \nUsted, {nom}, ha ganado!\n")
            break    
        else:
            cont=cont+1
            print(f"Número incorrecto, le quedan {10-cont} oportunidades.\n")
            
        if cont == 10:
            print("Intentarlo en otra ocasión. GAME OVER PAPÁ. \n")
            break

