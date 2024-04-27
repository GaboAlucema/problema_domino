
def valido(tablero, fila, col, direccion, siguiente):
    if direccion == "h":
        return  col + 1 < len(tablero[0]) and tablero[fila][col] == 0 and tablero[fila][siguiente] == 0:
    elif direccion == "v":
        return fila + 1 < len(tablero) and tablero[fila][col] == 0 and tablero[siguiente][col] == 0:
    return False

def colocar(tablero, fila, col, orientacion):
    if orientacion == "h":
        tablero[fila][col] = 1
        tablero[fila][col + 1] = 1
    elif orientacion == "v":
        tablero[fila][col] = 2
        tablero[fila + 1][col] = 2

def eliminar(tablero, fila, col, orientacion):
    if orientacion == "h":
        tablero[fila][col] = 0
        tablero[fila][col + 1] = 0
    elif orientacion == "v":
        tablero[fila][col] = 0
        tablero[fila + 1][col] = 0

def mostrar(tabla):
    for fila in tabla:
        print(' '.join(map(str,fila)))
    print()

def rellenar(tablero, fila, col, soluciones, orientacion_anterior=None):
    if fila == len(tablero):
        soluciones.append([fila[:] for fila in tablero])
        return
    
    sigfila = fila + (col + 1) // len(tablero[0])
    sigcol = (col + 1) % len(tablero[0])

    if orientacion_anterior == "h":
        if valido(tablero, fila, col, "v", sigfila):
            colocar(tablero, fila, col, "v")
            rellenar(tablero, sigfila, sigcol, soluciones)
            eliminar(tablero, fila, col, "v")

        if valido(tablero, fila, col, "h", sigcol):
            colocar(tablero, fila, col, "h")
            rellenar(tablero, sigfila, sigcol, soluciones)
            eliminar(tablero, fila, col, "h")
    else:
        if valido(tablero, fila, col, "h", sigcol):
            colocar(tablero, fila, col, "h")
            rellenar(tablero, sigfila, sigcol, soluciones)
            eliminar(tablero, fila, col, "h")
        if valido(tablero, fila, col, "v", sigfila):
            colocar(tablero, fila, col, "v")
            rellenar(tablero, sigfila, sigcol, soluciones)
            eliminar(tablero, fila, col, "v")
            

    rellenar(tablero, sigfila, sigcol, soluciones)

def encontrar_sol(fila,col):
    if (fila*col) % 2 != 0:
        print("No tiene solucion (producto de filas y columnas es impar)")
        return
    tablero = [[0] * col for _ in range(fila)]
    soluciones = []
    rellenar(tablero, 0, 0, soluciones)

    soluciones_validas = [solucion for solucion in soluciones if all (casilla != 0 for fila in solucion for casilla in fila)]
    
    if len(soluciones_validas) == 0:
        print("No se encontraron soluciones posibles.")
    else:
        print(f"Se encontraron {len(soluciones_validas)} soluciones posibles:")
        for i, solucion in enumerate(soluciones_validas):
            print(f"Solucion {i + 1}:")
            mostrar (solucion)


if __name__=="__main__":
    N = int(input("Ingrese el numero de filas: "))
    M = int(input("Ingrese el numero de columnas: "))

    encontrar_sol(N, M)
