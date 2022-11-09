"""
    NIVELES_DIFICULTAD: {
        FACIL: {
            6 PALABRAS,
            14x14,
            HORIZONTALES
        },
        INTERMEDIO: {
            7 PALABRAS,
            16x16,
            HORIZONTALES Y VERTICALES
        },
        DIFICIL: {
            8 PALABRAS,
            18x18,
            HORIZONTALES, VERTICALES.
        },
        EXTREMO: {
            12 PALABRAS,
            20x20,
            HORIZONTALES, VERTICALES Y AL REVES.
        }
    }
"""

import os
from random import randint

# Variables necesarias
archivo_palabras = None

try:
    archivo_palabras = open("palabras.txt")
except FileNotFoundError:
    print("[ERROR] Archivo no encontrado")
    pass

sopa_de_letras = []
palabras_seleccionadas = []
palabras_ingresadas = []
nivel_dificultad = [{ "palabras": 6, "cantidad_f_c": 14 },{ "palabras": 7, "cantidad_f_c": 16 },{ "palabras": 8, "cantidad_f_c": 18 },{ "palabras": 12, "cantidad_f_c": 20 }]
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
abecedario_especial = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Funcion para borrar la sopa de letras y actualizarla | PARAMETROS: {}
def borrar_consola():
    so = os.name

    if so == "posix":
        os.system("clear")
    elif so == "ce" or so == "nt" or so == "dos":
        os.system("cls")

# Funcion para mostrar las palabras restantes | PARAMETROS: {}
def mostrar_palabras_restantes():
    for palabra in palabras_ingresadas:
        orientacion = ''
        fila_columna = ''

        if palabra["orientacion"] == 0:
            orientacion = 'Horizontal'
            fila_columna = f"Fila: { palabra['fila'] + 1 }"
        else:
            orientacion = 'Vertical'
            fila_columna = f"Columna: { palabra['columna'] + 1 }"

        print(f"- { palabra['palabra'] } | {orientacion} | { fila_columna } | Inicia en: { palabra['inicio'] + 1 }")

# Funcion para resalatar la palabra encontrada en la sopa de letras | PARAMETROS: { 1: 'Informacion de palabra' }
def encontrar_palabra(palabra):
    caracteres_palabra = list(palabra["palabra"])
    caracteres_palabra_especial = []
    contador = 0

    if palabra["al_reves"] == 1:
        caracteres_palabra.reverse()

    for letra in caracteres_palabra:
        letra_index = abecedario.index(letra)
        caracter_especial = abecedario_especial[letra_index]
        caracteres_palabra_especial.append(caracter_especial)

    if palabra["orientacion"] == 0:
        for c in range(palabra["inicio"], len(sopa_de_letras)):
            try:
                sopa_de_letras[palabra["fila"]][c] = caracteres_palabra_especial[contador]
                contador += 1
            except IndexError:
                break
    elif palabra["orientacion"] == 1:
        for f in range(palabra["inicio"], len(sopa_de_letras)):
            try:
                sopa_de_letras[f][palabra["columna"]] = caracteres_palabra_especial[contador]
                contador += 1
            except IndexError:
                break

# Funcion para revisar si entra la palabra en esa posicion | PARAMETROS: { 1: 'Palabra', 2: 'Orientacion', 3: 'Inicio', 4: 'Fila / Columna' }
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

        print(palabra, orientacion, inicio, fila_columna)

    return entra

# Funcion para insertar palabras en horizontal | PARAMETROS: { 1: 'Palabra' }
def insertar_horizontal(palabra, dificultad):
    contador = 0
    caracteres_palabra = list(palabra)
    palabra_a_ingresar = palabra
    longitud_palabra = len(caracteres_palabra)
    longitud_sopa = len(sopa_de_letras) - 1
    fila = randint(0, longitud_sopa)
    al_reves = randint(0, 1)
    
    if dificultad == 3:
        if al_reves == 1:
            caracteres_palabra.reverse()
            palabra_a_ingresar = palabra[::-1]
    else:
        al_reves = 0

    if (longitud_sopa - longitud_palabra) > 0:
        inicio = randint(0, longitud_sopa  - longitud_palabra)
    else:
        inicio = 0
    
    while not revisar_posicion(palabra_a_ingresar, 0, inicio, fila):
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

        palabras_ingresadas.append({
            "palabra": palabra,
            "orientacion": 0,
            "fila": fila,
            "inicio": inicio,
            "al_reves": al_reves
        })
        
# Funcion para insertar palabras en vertical | PARAMETROS: { 1: 'Palabra' }
def insertar_vertical(palabra, dificultad):
    contador = 0
    caracteres_palabra = list(palabra)
    palabra_a_ingresar = palabra
    longitud_palabra = len(caracteres_palabra)
    longitud_sopa = len(sopa_de_letras) - 1
    columna = randint(0, longitud_sopa)
    al_reves = randint(0, 1)
    
    if dificultad == 3:
        if al_reves == 1:
            caracteres_palabra.reverse()
            palabra_a_ingresar = palabra[::-1]
    else:
        al_reves = 0

    if (longitud_sopa - longitud_palabra) > 0:
        inicio = randint(0, longitud_sopa  - longitud_palabra)
    else:
        inicio = 0

    while not revisar_posicion(palabra_a_ingresar, 1, inicio, columna):
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

        palabras_ingresadas.append({
            "palabra": palabra,
            "orientacion": 1,
            "columna": columna,
            "inicio": inicio,
            "al_reves": al_reves
        })

# Funcion para cerrar archivos | PARAMETROS: { 1: 'Archivo' }
def cerrar_archivo():
    try:
        archivo_palabras.close()
    except NameError:
        print("[ERROR] Archivo no encontrado")
        pass

# Funcion que por medio de recursividad busca una palabra | PARAMETROS: { 1: 'Cantidad caracteres' }
def buscar_palabra(cantidad_caracteres):
    nueva_palabra = archivo_palabras.readline().rstrip("\n")
    
    if len(nueva_palabra) <= cantidad_caracteres:
        if not nueva_palabra in palabras_seleccionadas:
            return nueva_palabra
        else:
            return buscar_palabra(cantidad_caracteres)
    else:
        return buscar_palabra(cantidad_caracteres)

# Funcion que devuelve cantidad de palabras en el archivo | PARAMETROS: {}
def contar_palabras():
    contador = 0

    while archivo_palabras.readline() != "":
        contador += 1

    archivo_palabras.seek(0)   
    return contador

# Funcion para mostrar la sopa de letras | PARAMETROS: {}
def mostrar_sopa():
    print()
    for fila in sopa_de_letras:
        for columna in fila:
            print("%4s" %columna, end="")
        print("\n")

# Funcion para seleccionar palabras del archivo | PARAMETROS: { 1: 'Nivel de dificultad' }
def seleccionar_palabras(dificultad):
    cantidad_palabras = contar_palabras()
    linea = archivo_palabras.readline()
    cantidad_f_c = nivel_dificultad[dificultad]["cantidad_f_c"]
    cantidad_palabras_seleccionadas = nivel_dificultad[dificultad]["palabras"]
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

    archivo_palabras.seek(0)       
    return palabras_seleccionadas
        
# Funcion para rellenar la matriz con letras alaeatorias | PARAMETROS: {}
def rellenar_matriz():
    for f in range(len(sopa_de_letras)):
        for c in range(len(sopa_de_letras)):
            if sopa_de_letras[f][c] == "":
                sopa_de_letras[f][c] = abecedario[randint(0,26)]

# Funcion para generar la sopa de letras | PARAMETROS: { 1: 'Nivel de dificultad' }
def generar_sopa(dificultad):
    palabras = seleccionar_palabras(dificultad)
    cantidad_f_c = nivel_dificultad[dificultad]["cantidad_f_c"]

    for f in range(cantidad_f_c):
        sopa_de_letras.append([])
        for c in range(cantidad_f_c):
            sopa_de_letras[f].append("")

    for palabra in palabras:
        orientacion = randint(0,1)

        if orientacion == 0:
            insertar_horizontal(palabra, dificultad)
        elif orientacion == 1:
            insertar_vertical(palabra, dificultad)
        
    rellenar_matriz()

# Funcion para preguntar al usuario la palabra encontrada | PARAMETROS: {}
def input_encontrar():
    print("Para salir del juego escribe 'salir', si no escribe la palabra que encontraste.")

    while len(palabras_ingresadas) > 0:
        palabra_encontrada = input("Ingresa palabra encontrada: ").lower()
        palabra_encontrada_info = {}
        encontrada = False

        if palabra_encontrada == 'salir':
            print("\n¿Por qué te vas antes de terminar? ¿No te há gustado el juego? :(\n")
            print(f"PALABRAS QUE FALTARON ENCONTRAR: { len(palabras_ingresadas) }")
            mostrar_palabras_restantes()
            print("\nJuego finalizado")
            break
 
        for palabra in palabras_ingresadas:
            if palabra["palabra"] == palabra_encontrada:
                encontrada = True
                palabra_encontrada_info = palabra
                break
            
        if encontrada:
            borrar_consola()
            print(f"Felicitaciones, encontraste la palabra '{ palabra_encontrada }'!")
            encontrar_palabra(palabra_encontrada_info)
            palabras_ingresadas.remove(palabra_encontrada_info)
            print(f"Te quedan por encontrar { len(palabras_ingresadas) } palabras!")
            print("\a\a")
            mostrar_sopa()
        else:
            print(f"La palabra '{ palabra_encontrada }' no existe en la sopa de letras")
    else:
        print("Felicitaciones, encontraste todas las palabras! Esperamos verte por aquí de nuevo!")

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

    print('\a')
    generar_sopa(dificultad - 1)
    cerrar_archivo()
    borrar_consola()
    mostrar_sopa()
    input_encontrar()

comenzar_juego()