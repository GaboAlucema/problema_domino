def imprimir(tabla,fila,col):
    for i in range(fila):
        for j in range(col):
            print(tabla[i][j], end=" ")
        print()

def valida(tabla, fila, col, i, j):
    if not (0 <= i < fila and 0 <= j < col and tabla[i][j] == 0):
        return False
    
    if j > 0 and tabla[i][j - 1] != 0:
        return False
    if i > 0 and tabla[i - 1][j] != 0:
        return False
    
    return True

def colocar(tabla, i, j, forma):
    if forma == 'v':
        tabla[i][j] = 'r'
        tabla[i + 1][j] = 'r'
    elif forma == 'h':
        tabla[i][j] = 'a'
        tabla[i][j + 1] = 'a'

def quitar(tabla, i, j, forma):
    if forma == 'v':
        tabla[i][j] = '0'
        tabla[i + 1][j] = '0'
    elif forma == 'h':
        tabla[i][j] = '0'
        tabla[i][j + 1] = '0'

def solucion(tabla, fila, col, i, j):
    if(i == fila):
        return True
    
    sigj = (j + 1) % col
    sigi = i

    if sigj == 0:
        sigj = 0
        sigi += 1

    if tabla[i][j] == 0 and valida(tabla, fila, col, i + 1, j):
        colocar(tabla, i, j, 'v')
        if solucion(tabla, fila, col, sigi, sigj):
            return True
        quitar(tabla, i, j, 'v')

    if tabla[i][j] == 0 and valida(tabla, fila, col, i, j + 1):
        colocar(tabla, i, j, 'h')
        if j + 1 == col:
            sigi = i + 1
            sigj = 0        
        if solucion(tabla, fila, col, sigi, sigj):
            return True
        quitar(tabla, i, j, 'h')

    if tabla[i][j] == 0:
        return solucion(tabla, fila, col, sigi, sigj)

    return False

if __name__ == "__main__":
    row = 5
    col = 6
    tablero = [[0 for y in range(col)] for x in range(row)]

    if((row * col) % 2 == 0):
        if(solucion(tablero, row, col, 0, 0)):
            imprimir(tablero, row, col)
        else:
            print("No tiene solucion")
    else:
        print("No tiene solucion")
