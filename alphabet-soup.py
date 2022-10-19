"""
    NIVELES_DIFICULTAD: {
        FACIL: {
            10 PALABRAS,
            10x10,
            HORIZONTALES Y VERTICALES
        },
        INTERMEDIO: {
            12 PALABRAS,
            12x12,
            HORIZONTALES, VERTICALES Y DIAGONALES
        },
        DIFICIL: {
            14 PALABRAS,
            14x14,
            HORIZONTALES, VERTICALES, DIAGONALES Y PALABRAS ESCRITAS AL REVES
        },
        EXTREMO: {
            20 PALABRAS,
            20x20,
            HORIZONTALES, VERTICALES, DIAGONALES Y PALABRAS ESCRITAS AL REVES
        }
    }
"""

from random import randint

# Variables necesarias
sopa_de_letras = []
palabras_seleccionadas = []
nivel_dificultad = [10, 12, 14, 20]
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Funcion que por medio de recursividad busca una palabra | PARAMETROS: { 1: 'Palabra' }
def buscar_palabra(cantidad_caracteres):
    archivo = open('palabras.txt')
    nueva_palabra = archivo.readline().rstrip("\n")

    if len(nueva_palabra) <= cantidad_caracteres:
        if not nueva_palabra in palabras_seleccionadas:
            return nueva_palabra
        else:
            return buscar_palabra(cantidad_caracteres)
    else:
        return buscar_palabra(cantidad_caracteres)
        
# Funcion que devuelve cantidad de palabras en el archivo | PARAMETROS: {}
def contar_palabras():
    archivo = open("palabras.txt")
    contador = 0

    while archivo.readline() != "":
        contador += 1

    archivo.close()

    return contador

# Funcion para mostrar la sopa de letras | PARAMETROS: { 1: 'Matriz de sopa de letras' }
def mostrar_sopa(sopa):
    print()
    for fila in sopa:
        for columna in fila:
            print("%4s" %columna, end="")
        print("\n")

# Funcion para seleccionar palabras del archivo | PARAMETROS: { 1: 'Nivel de dificultad' }
def seleccionar_palabras(dificultad):
    cantidad_palabras = contar_palabras()
    cantidad_caracteres = nivel_dificultad[dificultad - 1]

    archivo = open("palabras.txt")
    linea = archivo.readline()

    contador = 0
    
    n1 = randint(0, cantidad_palabras - cantidad_caracteres) 
    n2 = n1 + cantidad_caracteres

    while linea:
        palabra = linea.rstrip("\n")
        
        if contador >= n1 and contador < n2:
            if len(palabra) > cantidad_caracteres:
                nueva_palabra = buscar_palabra(cantidad_caracteres)
                palabras_seleccionadas.append(nueva_palabra)
            else:
                palabras_seleccionadas.append(palabra)

        contador += 1
        linea = archivo.readline()

    archivo.close()
    return palabras_seleccionadas

# Funcion para generar la sopa de letras | PARAMETROS: { 1: 'Nivel de dificultad' }
def generar_sopa(dificultad):
    palabras = seleccionar_palabras(dificultad)
    cantidad_f_c = nivel_dificultad[dificultad - 1]

    for f in range(cantidad_f_c):
        sopa_de_letras.append([])
        for c in range(cantidad_f_c):
            sopa_de_letras[f].append("")

    for index, palabra in enumerate(palabras):
        lista_caracteres = list(palabra)

        for c in range(cantidad_f_c):
            try:
                sopa_de_letras[index][c] = lista_caracteres[c]
            except IndexError:
                sopa_de_letras[index][c] = abecedario[randint(0,26)]

    mostrar_sopa(sopa_de_letras)

# Funcion para comenzar el juego | PARAMETROS: {}
def comenzar_juego():
    print("Hola! Bienvenido a la 'Sopa de letras' en python, esperamos que te diviertas.")
    print("\nNiveles de dificultad:\n1. Facil\n2. Intermedio\n3. Dificil\n4. Extremo")

    dificultad = 0

    while (dificultad < 1 or dificultad > 4):
        try:
            dificultad = int(input("Ingrese numero de nivel dificultad para comenzar: "))
        except ValueError:
            print("[ERROR] Debes ingresar un nivel de dificultad valido entre 1 y 4.")

    generar_sopa(dificultad)

if __name__ == '__main__':
    comenzar_juego()