# En la primera solución el usuario adivinara sin ayuda el numero en un rango del 1 al 20
#  El sistema mostrara un mensaje de bienvenida con el nombre el jugador
#  Llevara un registro de los intentos realizado por el jugador
#  En la segunda solución el usuario adivinara con cierta cantidad de oportunidades y con
#   la ayuda del sistema que indicara si esta por arriba o por debajo del numero

import funciones

if __name__=="__main__":

    funciones.nom
    print("")
    option=0

    while not option == 3:   

        op=input("Ingresar una opción: \n1- Juego modo fácil (Con ayuda)\n2- Juego modo difícil (Sin ayuda)\n3- Salir\n")
        print("")
        while not op.isnumeric():
            op=input("Ingresar una opción numérica: \n1- Juego modo fácil\n2- Juego modo dificil\n3- Salir\n")
            print("")
        option=int(op)

        if option == 1:
            funciones.modofacil()
        elif option == 2:
            funciones.mododificil()
            
    print("""
    ###################################
    #                                 #
    #        Gracias por jugar        #
    #                                 #
    ###################################
    """)
    
            
