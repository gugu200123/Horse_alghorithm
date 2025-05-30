N = 8

def eh_seguro(x, y, tabuleiro):
    return 0 <= x < N and 0 <= y < N and tabuleiro[x][y] == -1

def imprimir_solucao(tabuleiro):
    print("Solução para o Passeio do Cavalo:")
    for i in range(N):
        for j in range(N):
            print(f"{tabuleiro[i][j]:>3}", end="")
        print()

def conta_movimentos_possiveis(x, y, tabuleiro, movimentos_x, movimentos_y):
    contador = 0
    for i in range(8):
        prox_x = x + movimentos_x[i]
        prox_y = y + movimentos_y[i]
        if eh_seguro(prox_x, prox_y, tabuleiro):
            contador += 1
    return contador

def resolver_passeio():
    tabuleiro = [[-1 for i in range(N)] for i in range(N)]

    movimentos_x = [2, 1, -1, -2, -2, -1, 1, 2]
    movimentos_y = [1, 2, 2, 1, -1, -2, -2, -1]

    x_atual, y_atual = 0, 0
    tabuleiro[x_atual][y_atual] = 0

    for i in range(1, N * N):
        min_grau_idx = -1
        min_grau = N + 1
        
        for k in range(8):
            prox_x = x_atual + movimentos_x[k]
            prox_y = y_atual + movimentos_y[k]

            if eh_seguro(prox_x, prox_y, tabuleiro):
                grau_atual = conta_movimentos_possiveis(prox_x, prox_y, tabuleiro, movimentos_x, movimentos_y)
                
                if grau_atual < min_grau:
                    min_grau_idx = k
                    min_grau = grau_atual

        if min_grau_idx == -1:
            print("Não foi encontrada uma solução a partir deste ponto.")
            return False

        x_atual += movimentos_x[min_grau_idx]
        y_atual += movimentos_y[min_grau_idx]
        tabuleiro[x_atual][y_atual] = i
    
    imprimir_solucao(tabuleiro)
    return True

if __name__ == "__main__":
    resolver_passeio()
