import os

def verificar_palabra_ingresada(palabra_a_encontrar, palabra_ingresada):
    # Crear una lista vacía para el resultado.
    # Si las letras existen en la palabra a encontrar y sus posiciones coinciden: Encerrarlas en [] y agregar al resultado.
    # Si las letras existen en la palabra a encontrar pero sus posiciones no coinciden: Encerrarlas en () y agregar al resultado.
    # Si no se cumple ninguna de las anteriores, agregar al resultado sin hacer modificaciones.
    # Retornar el resultado.


    resultado = [] # Creamos una lista vacía para almacenar el resultado de una linea

    for posicion in range(cantidad_de_letras): # Iteramos por cada letra de la palabra ingresada

        las_letras_son_iguales = palabra_a_encontrar[posicion] == palabra_ingresada[posicion]

        la_letra_existe_en_la_palabra_a_encontrar = palabra_ingresada[posicion] in palabra_a_encontrar
        
        if las_letras_son_iguales:
            # guardar las letras que están en la palabra a encontrar y coinciden en la posición, dentro de brackets
            resultado.append('['+ palabra_ingresada[posicion] +']')

        elif la_letra_existe_en_la_palabra_a_encontrar:
            # guardar las letras que no coinciden pero que están en la palabra a encontrar, dentro de parentesis
            resultado.append('('+ palabra_ingresada[posicion] +')')

        else:
            # Las que no coinciden, se guardan sin modificiaciones
            resultado.append(palabra_ingresada[posicion])

    return resultado


def imprimir_grilla(grilla):
    cantidad_de_filas = len(grilla)

    for fila in range(cantidad_de_filas):
        print(grilla[fila])


# Ejecución del programa

palabra_a_encontrar = "perro"
cantidad_de_letras = 5
intentos = 6

grilla = []

os.system('cls')
print("Bienvenido a Wordle!")

while intentos > 0:
    print("Te quedan", intentos, "intentos.")
    palabra_ingresada = input("Ingrese una palabra: ")
    intentos = intentos - 1

    os.system('cls')

    if(len(palabra_ingresada) != cantidad_de_letras):
        print("La palabra ingresada no tiene la cantidad de letras correcta.")
        print(" Ingresar una palabra con", cantidad_de_letras, "letras.")
        continue
    else:
        linea_verificada = verificar_palabra_ingresada(palabra_a_encontrar, palabra_ingresada)
        grilla.append(linea_verificada)

    imprimir_grilla(grilla)
    if palabra_ingresada == palabra_a_encontrar:
        print("Felicidades, ganaste. 🍫")
        break