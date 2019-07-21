def mult(M, N):
    columnM = len(M[0])
    rowN = len(N)
    if columnM == rowN:
        matrix = []
        resultado = []
        for linha in range(len(M)):
            for coluna in range(len(N[0])):
                soma = 0
                for k in range(len(N)):
                    soma += M[linha][k] * N[k][coluna]
                matrix += [soma,]
            resultado += [matrix,]
            matrix = []
        return resultado
    else:
        return []