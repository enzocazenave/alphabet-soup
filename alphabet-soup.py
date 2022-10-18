from random import randint

# Variables necesarias
sopa_de_letras = []

# Funcion para mostrar la sopa de letras | ARGS: { 1: 'Matriz de sopa de letras' }
def mostrar_sopa(sopa):
    for fila in sopa:
        for columna in fila:
            print(columna, end=" ")
        print()

# Funcion para seleccionar palabras del archivo | ARGS: { 1: 'Nivel de dificultad' }
def seleccionar_palabras(dificultad):
    palabras_seleccionadas = []

    archivo = open("palabras.txt", "rt")
    linea = archivo.readline()

    contador = 0

    n1 = 5
    n2 = 14

    while linea:
        palabra = linea.rstrip("\n")
        linea = archivo.readline()
        
        if contador >= n1 and contador <= n2:
            palabras_seleccionadas.append(palabra)

        contador += 1


# Funcion para generar la sopa de letras | Args: { 1: 'Nivel de dificultad' }
def generar_sopa(dificultad):
    palabras = seleccionar_palabras(dificultad)

# Funcion para comenzar el juego | ARGS: {}
def comenzar_juego():
    print("Hola! Bienvenido a la 'Sopa de letras' en python, esperamos que te diviertas.")
    print("\nNiveles de dificultad:\n1. Facil\n2. Intermedio\n3. Dificil\n4. Extremo")

    dificultad = 0

    while (dificultad < 1 or dificultad > 4):
        try:
            dificultad = int(input("Ingrese numero de nivel dificultad para comenzar: "))
        except ValueError:
            print("[ERROR] Debes ingresar un nivel de dificultad valido.")

    generar_sopa(dificultad)

if __name__ == '__main__':
    comenzar_juego()
