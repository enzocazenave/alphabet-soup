"""
    NIVELES_DIFICULTAD: {
        FACIL: {
            6 PALABRAS,
            10x10,
            HORIZONTALES
        },
        INTERMEDIO: {
            7 PALABRAS,
            12x12,
            HORIZONTALES Y VERTICALES
        },
        DIFICIL: {
            8 PALABRAS,
            14x14,
            HORIZONTALES, VERTICALES Y DIAGONALES
        },
        EXTREMO: {
            12 PALABRAS,
            20x20,
            HORIZONTALES, VERTICALES, DIAGONALES Y PALABRAS ESCRITAS AL REVES
        }
    }
"""

from random import randint

# Variables necesarias
archivo_palabras = open("palabras.txt")
sopa_de_letras = []
palabras_seleccionadas = []
nivel_dificultad = [{ "palabras": 6, "cantidad_f_c": 12 },{ "palabras": 7, "cantidad_f_c": 14 },{ "palabras": 8, "cantidad_f_c": 16 },{ "palabras": 12, "cantidad_f_c": 20 }]
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Funcion para revisar si entre la palabra en esa posicion | PARAMETROS: { 1: 'Palabra', 2: 'Orientacion', 3: 'Inicio', 4: 'Fila / Columna' }
def revisar_posicion(palabra, orientacion, inicio, fila_columna):
    entra = False
    contador = 0
    caracteres_palabra = list(palabra)

    if orientacion == 0:
        for c in range(inicio, len(sopa_de_letras)):
            try: 
                if sopa_de_letras[fila_columna][c] != caracteres_palabra[contador]:
                    if sopa_de_letras[fila_columna][c] == "":
                        entra = True
                        contador += 1
                    else:
                        entra = False
                        break
                else:
                    entra = True
                    contador += 1
            except IndexError:
                break
    elif orientacion == 1:
        for f in range(inicio, len(sopa_de_letras)):
            try:
                if sopa_de_letras[f][fila_columna] != caracteres_palabra[contador]:
                    if sopa_de_letras[f][fila_columna] == "":
                        entra = True
                        contador += 1
                    else:
                        entra = False
                        break
                else:
                    entra = True
                    contador += 1
            except IndexError:
                break

    return entra
            
# Funcion para insertar palabras en horizontal | PARAMETROS: { 1: 'Palabra' }
def insertar_horizontal(palabra):
    contador = 0
    caracteres_palabra = list(palabra)
    longitud_palabra = len(caracteres_palabra)
    longitud_sopa = len(sopa_de_letras)
    fila = randint(0, longitud_sopa)
    
    if (longitud_sopa - longitud_palabra) > 0:
        inicio = randint(0, longitud_sopa  - longitud_palabra)
    else:
        inicio = 0

    while not revisar_posicion(palabra, 0, inicio, fila):
        fila = randint(0, longitud_sopa)

        if (longitud_sopa - longitud_palabra) > 0:
            inicio = randint(0, longitud_sopa  - longitud_palabra)
        else:
            inicio = 0
    else:
        for c in range(inicio, len(sopa_de_letras)):
            try:
                if sopa_de_letras[fila][c] != caracteres_palabra[contador]:
                    sopa_de_letras[fila][c] = caracteres_palabra[contador]
                    contador += 1
                else:
                    contador += 1
            except IndexError:
                break
        
# Funcion para insertar palabras en vertical | PARAMETROS: { 1: 'Palabra' }
def insertar_vertical(palabra):
    contador = 0
    caracteres_palabra = list(palabra)
    longitud_palabra = len(caracteres_palabra)
    longitud_sopa = len(sopa_de_letras)
    columna = randint(0, longitud_sopa)
    
    if (longitud_sopa - longitud_palabra) > 0:
        inicio = randint(0, longitud_sopa  - longitud_palabra)
    else:
        inicio = 0

    while not revisar_posicion(palabra, 1, inicio, columna):
        columna = randint(0, longitud_sopa)

        if (longitud_sopa - longitud_palabra) > 0:
            inicio = randint(0, longitud_sopa  - longitud_palabra)
        else:
            inicio = 0
    else:
        for f in range(inicio, len(sopa_de_letras)):
            try:
                if sopa_de_letras[f][columna] != caracteres_palabra[contador]:
                    sopa_de_letras[f][columna] = caracteres_palabra[contador]
                    contador += 1
                else:
                    contador += 1
            except IndexError:
                break

# Funcion para cerrar archivos | PARAMETROS: { 1: 'Archivo' }
def cerrar_archivo():
    try:
        archivo_palabras.close()
    except NameError:
        print("[ERROR] Archivo no encontrado")
        pass

# Funcion que por medio de recursividad busca una palabra | PARAMETROS: { 1: 'Cantidad caracteres' }
def buscar_palabra(cantidad_caracteres):
    try:
        nueva_palabra = archivo_palabras.readline().rstrip("\n")

        if len(nueva_palabra) <= cantidad_caracteres:
            if not nueva_palabra in palabras_seleccionadas:
                return nueva_palabra
            else:
                return buscar_palabra(cantidad_caracteres)
        else:
            return buscar_palabra(cantidad_caracteres)
    except:
        print("[ERROR] Ocurrio un error al abrir el archivo")     

# Funcion que devuelve cantidad de palabras en el archivo | PARAMETROS: {}
def contar_palabras():
    try:
        contador = 0

        while archivo_palabras.readline() != "":
            contador += 1

        return contador
    except:
        print("[ERROR] Ocurrio un error al abrir el archivo")
    finally:
        archivo_palabras.seek(0)       


# Funcion para mostrar la sopa de letras | PARAMETROS: {}
def mostrar_sopa():
    print()
    for fila in sopa_de_letras:
        for columna in fila:
            print("%4s" %columna, end="")
        print("\n")

# Funcion para seleccionar palabras del archivo | PARAMETROS: { 1: 'Nivel de dificultad' }
def seleccionar_palabras(dificultad):
    try:
        linea = archivo_palabras.readline()

        cantidad_palabras = contar_palabras()
        cantidad_f_c = nivel_dificultad[dificultad - 1]["cantidad_f_c"]
        cantidad_palabras_seleccionadas = nivel_dificultad[dificultad - 1]["palabras"]

        contador = 0

        n1 = randint(0, cantidad_palabras - cantidad_palabras_seleccionadas) 
        n2 = n1 + cantidad_palabras_seleccionadas

        while linea:
            palabra = linea.rstrip("\n")

            if contador >= n1 and contador < n2:
                if len(palabra) > cantidad_f_c:
                    nueva_palabra = buscar_palabra(cantidad_f_c)
                    palabras_seleccionadas.append(nueva_palabra)
                else:
                    palabras_seleccionadas.append(palabra)

            contador += 1
            linea = archivo_palabras.readline()

        return palabras_seleccionadas
    except:
        print("[ERROR] Ocurrio un error al abrir el archivo")
    finally:
        archivo_palabras.seek(0)       

def rellenar_matriz():
    for f in range(len(sopa_de_letras)):
        for c in range(len(sopa_de_letras)):
            if sopa_de_letras[f][c] == "":
                sopa_de_letras[f][c] = "-"#abecedario[randint(0,26)]

# Funcion para generar la sopa de letras | PARAMETROS: { 1: 'Nivel de dificultad' }
def generar_sopa(dificultad):
    palabras = seleccionar_palabras(dificultad)
    cantidad_f_c = nivel_dificultad[dificultad - 1]["cantidad_f_c"]

    for f in range(cantidad_f_c):
        sopa_de_letras.append([])
        for c in range(cantidad_f_c):
            sopa_de_letras[f].append("")

    for palabra in palabras:
        orientacion = randint(0,1)

        if orientacion == 0:
            insertar_horizontal(palabra)
        elif orientacion == 1:
            insertar_vertical(palabra)
        
    rellenar_matriz()

# Funcion para comenzar el juego | PARAMETROS: {}
def comenzar_juego():
    print("\nHola! Bienvenido a la 'Sopa de letras' en python, esperamos que te diviertas.")
    print("\nNiveles de dificultad:\n1. Facil\n2. Intermedio\n3. Dificil\n4. Extremo\n")

    dificultad = 0

    while (dificultad < 1 or dificultad > 4):
        try:
            dificultad = int(input("Ingrese numero de nivel dificultad para comenzar: "))
        except ValueError:
            print("[ERROR] Debes ingresar un nivel de dificultad valido entre 1 y 4.")

    generar_sopa(dificultad)
    cerrar_archivo()
    mostrar_sopa()

if __name__ == '__main__':
    comenzar_juego()