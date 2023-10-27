def laberinto(dimension, obstaculos):
    ''' Función que construye un laberinto cuadrado de una dimensión dada poniendo.

    Parámetros requeridos:
        - dimension: cantidad de columnas y filas usaremos un unico valor que siempregenerara una matriz cuadrada
        - obstaculos: Es una lista de tuplas con posiciones donde hay obstaculos.

    Salida: 
        Una matriz que representa el laberinto. 
    '''

    # Creamos una lista vacía para añadir las filas del laberinto.
    laberinto = []
    # Bucle  para añadir las filas del laberinto.
    for i in range(dimension):
        # Creamos una lista vacía para añadir las casillas de la fila.
        fila = []
        # Bucle  para recorrer las columnas del laberinto.
        for j in range(dimension):
            # Comprobar si la tupla está en el la lista de obstaculos.
            if tuple([i, j]) in obstaculos:
                fila.append('X')
            else:
                fila.append('0')
        laberinto.append(fila)
    return laberinto

def recorre_laberinto(laberinto):
    
    
    n = len(laberinto)  
    fila = columna = 0  
    movimientos = [] #Indica la lista de movimientos.

    while fila < n - 1 or columna < n - 1:         #Esta condición asegura que el ciclo continúe mientras las coordenadas fila y columna estén dentro de los limites del laberinto.
        if (len(movimientos) == 0 or movimientos[-1] != 'Arriba') and fila + 1 < n and laberinto[fila + 1][columna] != 'X':
            fila += 1
            movimientos.append('Abajo')
        elif (len(movimientos) == 0 or movimientos[-1] != 'Abajo') and fila - 1 >= 0 and laberinto[fila - 1][columna] != 'X':         #Estas condiciones el if y elif determinan si el movimiento siguiente 
            fila -= 1                                                                                                                  # es válido y si se ha movido en una dirección específica previamente.
            movimientos.append('Arriba')                                                                                                    
        elif (len(movimientos) == 0 or movimientos[-1] != 'Izquierda') and columna + 1 < n and laberinto[fila][columna + 1] != 'X':     #Si la condición se cumple, se actualizan las coordenadas y se
            columna += 1                                                                                                                 # agrega el movimiento correspondiente a la lista de movimientos.
            movimientos.append('Derecha')
        elif (len(movimientos) == 0 or movimientos[-1] != 'Derecha') and columna - 1 >= 0 and laberinto[fila][columna - 1] != 'X':
            columna -= 1
            movimientos.append('Izquierda')
        else:
            # No hay salida a movimientos y se rompe el ciclo while con break.
            movimientos.append('No hay salida')
            break

    return movimientos #Se retorna la lista de movimientos que contiene los movimientos realizados en el laberinto.

# Tupla de posisiones de las celdas con obstaculos en el laberinto
obstaculo = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) 
# Tamaño de la matriz
dimension = 5
# llamada a la funcion una vez establecidos los valores de obstaculos
lab = laberinto(dimension, obstaculo)   

# Imprimnir el laberinto
# SOLO COMO EJEMPLO
for i in lab:
    print(''.join(i))

print("Resultado")
for movimiento in resultado:
    print(movimiento)

# Esperamos al usuario
input("presione enter para salir")