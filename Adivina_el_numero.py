"""
Proyecto basico de Python (Juego)

Adivina el numero: El juego consiste en adivinar un numero del 1 al 100, se pueden hacer infinitos intentos hasta dar con el numero aleatorio generado por la computadora.

"""



import random

def adivina_el_numero (x):
    
    print ("===========================================")
    print ("        ¡Bienvenid(a) al Juego!"            )
    print ("===========================================")
    print ("Tu objetivo es adivinar el numero generado por la computadora.")
    
    numero_aleatorio = random.randint (1, x) #Numero aleatorio entre 1 y x...
    
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        # El jugador ingresa un numero...
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))
    
        if prediccion < numero_aleatorio:
            print ("mmm... pensá en un numero mas alto...")
        elif prediccion > numero_aleatorio:
            print ("mmm... probá con un numero mas bajo... ")
    
    print (f"¡Felicitaciones! Adivinaste el numero {numero_aleatorio} correctamente :)")

# Llamando a la funcion...
adivina_el_numero(100)    
        
