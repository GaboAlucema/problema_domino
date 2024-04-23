
def valido(tablero, fila, col):
    return tablero[fila][col] == 0

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

def rellenar(tablero, fila, col, soluciones):
    if fila == len(tablero):
        soluciones.append([fila[:] for fila in tablero])
        return
    
    sigfila = fila + (col + 1) // len(tablero[0])
    sigcol = (col + 1) % len(tablero[0])

    if valido(tablero, fila, col):
        colocar(tablero, fila, col, "h")
        rellenar(tablero, sigfila, sigcol, soluciones)
        eliminar(tablero, fila, col, "h")

        colocar(tablero, fila, col, "v")
        rellenar(tablero, sigfila, sigcol, soluciones)
        eliminar(tablero, fila, col, "v")

    else:
        rellenar(tablero, sigfila, sigcol, soluciones)

def solucion(fila,col):
    if (fila*col)%2!=0:
        print("No tiene solucion (producto de filas y columnas es impar)")
        return
    tablero = [[0] * col for _ in range(fila)]
    soluciones = []
    rellenar(tablero, 0, 0, soluciones)


if __name__=="__main__":
    N = int(input("Ingrese el numero de filas: "))
    M = int(input("Ingrese el numero de columnas"))

    solucion(N, M)