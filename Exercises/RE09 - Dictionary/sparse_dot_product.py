def sparse_dot_product(dict1, dict2):
    soma = 0
    for i1 in dict1:            
            if i1 in dict2: 
                soma += (dict1[i1]*dict2[i1]) 
    return soma