def mostrar (matriz, fila, col):
    for i in range(fila):
        for j in range(col):
            print(matriz[i][j], end = " ")
        print()


if __name__=="__main__":
    N = 3
    M = 4

    matriz = [[0 for _ in range(M)] for _ in range(N)]

    mostrar(matriz, N, M)