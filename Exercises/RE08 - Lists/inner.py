def inner(u, v):
    soma = 0
    for idx, i in enumerate(u):
            result = i * v[idx]
            soma += result
    return soma