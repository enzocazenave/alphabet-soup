# Variables necesarias
sopa_de_letras = []

# Funcion para mostrar la sopa de letras | ARGS: { 1: 'Matriz de sopa de letras' }
def mostrar_sopa(sopa):
    for fila in sopa:
        for columna in fila:
            print(columna, end=" ")
        print()