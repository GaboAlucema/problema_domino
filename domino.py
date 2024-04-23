
def valido(tablero, fila, col):
    return tablero[fila][col] == 0

def rellenar(tablero, fila, col, soluciones):
    if fila == len(tablero):
        soluciones.append([fila[:] for fila in tablero])
        return
    
    sigfila = fila + (col + 1) // len(tablero[0])
    sigcol = (col + 1) % len(tablero[0])

    if valido(tablero, fila, col):
        colocar()
        rellenar(tablero, sigfila, sigcol, soluciones)
        eliminar()


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