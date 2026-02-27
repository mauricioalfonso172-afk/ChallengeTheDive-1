#importamos la libreria "time" para poder hacer la cuenta regresiva.
import time

# Wins
def excelente():
    print (f'Felicidades haz ganado, tienes 3/3 estrellas.')

def bien():
    print (f'Bien hecho, tienes 2/3 estrellas.')

def meh():
    print (f'haz obtenido 1/3 estrellas.')

# Defeat
def gameover():
    print (f'GAME OVER, Obtienes 0/3 estrellas, mala suerte... ')

# Definimos Variables 
raton = "🐭"
R = raton

gato = "🐱"
G = gato

queso = "🧀"
Q = queso

meta = "M"
M = meta

pared = "#"
P = pared

vacio = '.'
V = vacio

# --- ESTADOS NUEVOS ---
tiene_queso = False
turno_raton_extra = 0
juego_terminado = False
tiempo_queso = None
tiempo_meta = None

# Definimos una tabla (mejor distribuida visualmente).
tablero = [
    [P,P,P,P,P,P,P,P,P],
    [P,G,V,V,P,V,Q,V,P],
    [P,V,P,V,P,V,P,V,P],
    [P,V,P,V,V,V,P,V,P],
    [P,V,P,P,P,V,P,V,P],
    [P,V,V,V,P,V,V,V,P],
    [P,P,P,V,P,P,P,V,P],
    [P,M,V,V,V,V,P,V,P],
    [P,V,P,P,P,V,P,V,P],
    [P,P,P,P,P,P,P,R,P]
]

def distancia_manhattan(f1, c1, f2, c2):
    return abs(f1 - f2) + abs(c1 - c2)

#funcion que hace una cuenta atras.
def cuenta_atras():
    duracion = 300
    tiempo_restante = int(duracion - (tiempo_actual - tiempo_inicio)) 
    if tiempo_restante <= 0:
        gameover()
        exit()
    minutos = tiempo_restante // 60
    segundos = tiempo_restante % 60
    print (f"Tiempo")
    print (f"╔══════════════════════╗")
    print (f"║{minutos:02}:{segundos:02}║")
    print (f"╚══════════════════════╝")

print (f"╔══════════════════════╗")
print (f"║05:00                 ║")
print (f"╚══════════════════════╝")

#funcion que imprime el tablero.
def mostrar_tablero(turno_texto=""):
    print (f"--- {turno_texto} ---")
    for fila in tablero:
        print(" ".join(fila))

#Establecemos el tiempo de inicio.
tiempo_inicio = time.time()

movimientos_gato = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

def minimax(tablero, fila_gato, col_gato, fila_raton, col_raton, profundidad, es_turno_gato):
    
    if fila_gato == fila_raton and col_gato == col_raton:
        return 1000  

    if profundidad == 0:
        distancia = distancia_manhattan(fila_gato, col_gato, fila_raton, col_raton)
        return -distancia

    if es_turno_gato:
        mejor_valor = -99999

        for mov in movimientos_gato:
            nueva_fila = fila_gato + mov[0]
            nueva_col = col_gato + mov[1]

            if (0 <= nueva_fila < len(tablero)) and \
               (0 <= nueva_col < len(tablero[0])) and \
               tablero[nueva_fila][nueva_col] != P:

                valor = minimax(
                    tablero,
                    nueva_fila,
                    nueva_col,
                    fila_raton,
                    col_raton,
                    profundidad - 1,
                    False
                )

                mejor_valor = max(mejor_valor, valor)

        return mejor_valor

    else:
        peor_valor = 99999
        movimientos_raton = [(-1,0),(1,0),(0,-1),(0,1)]

        for mov in movimientos_raton:
            nueva_fila = fila_raton + mov[0]
            nueva_col = col_raton + mov[1]

            if (0 <= nueva_fila < len(tablero)) and \
               (0 <= nueva_col < len(tablero[0])) and \
               tablero[nueva_fila][nueva_col] != P:

                valor = minimax(
                    tablero,
                    fila_gato,
                    col_gato,
                    nueva_fila,
                    nueva_col,
                    profundidad - 1,
                    True
                )

                peor_valor = min(peor_valor, valor)

        return peor_valor

def mejor_movimiento_gato():
    global fila_gato, columna_gato
    mejor_valor = -99999
    mejor_mov = None

    for mov in movimientos_gato:
        nueva_fila = fila_gato + mov[0]
        nueva_col = columna_gato + mov[1]

        if (0 <= nueva_fila < len(tablero)) and \
           (0 <= nueva_col < len(tablero[0])) and \
           tablero[nueva_fila][nueva_col] != P:

            valor = minimax(
                tablero,
                nueva_fila,
                nueva_col,
                fila_raton,
                columna_raton,
                3,
                False
            )

            if valor > mejor_valor:
                mejor_valor = valor
                mejor_mov = (nueva_fila, nueva_col)

    return mejor_mov

#funcion que acrualiza el tablero.
def actualizar_tablero(turno_texto):
    print("\n----------------------------------")
    cuenta_atras()
    print("\n----------------------------------")
    mostrar_tablero(turno_texto)

# Posición inicial raton
fila_raton = 9
columna_raton = 7

# Posicion Inicial Gato
fila_gato = 1
columna_gato = 1

turno_actual = "RATON"

# Mostrar tablero inicial.
mostrar_tablero("TURNO DEL RATON")

# Bucle del juego
while not juego_terminado:
    tiempo_actual = time.time()

    # --- TURNO RATON ---
    if turno_actual == "RATON":
        movimiento = input("Mueva con S/W/A/D, X salir: ")

        if movimiento.upper() == "X":
            break

        nueva_fila = fila_raton
        nueva_columna = columna_raton

        if movimiento.upper() == "W":
            nueva_fila -= 1
        if movimiento.upper() == "S":
            nueva_fila += 1
        if movimiento.upper() == "A":
            nueva_columna -= 1
        if movimiento.upper() == "D":
            nueva_columna += 1

        if (0 <= nueva_fila < len(tablero)) and \
           (0 <= nueva_columna < len(tablero[0])) and \
           tablero[nueva_fila][nueva_columna] != P:

            destino = tablero[nueva_fila][nueva_columna]

            tablero[fila_raton][columna_raton] = V
            tablero[nueva_fila][nueva_columna] = R
            fila_raton = nueva_fila
            columna_raton = nueva_columna

            if destino == Q and not tiene_queso:
                tiene_queso = True
                turno_raton_extra = 1
                tiempo_queso = int(tiempo_actual - tiempo_inicio)

            if destino == M:
                tiempo_meta = int(tiempo_actual - tiempo_inicio)
                if tiene_queso and tiempo_meta <= 120:
                    excelente()
                elif tiene_queso:
                    bien()
                else:
                    meh()
                juego_terminado = True
                break

        if fila_gato == fila_raton and columna_gato == columna_raton:
            gameover()
            break

        if turno_raton_extra > 0:
            turno_raton_extra -= 1
            turno_actual = "RATON"
        else:
            turno_actual = "GATO"

        actualizar_tablero("TURNO DEL RATON")

    # --- TURNO GATO ---
    else:
        mov_gato = mejor_movimiento_gato()

        if mov_gato is not None:
            tablero[fila_gato][columna_gato] = V
            fila_gato, columna_gato = mov_gato
            tablero[fila_gato][columna_gato] = G

        if fila_gato == fila_raton and columna_gato == columna_raton:
            gameover()
            break

        turno_actual = "RATON"
        actualizar_tablero("TURNO DEL GATO")
