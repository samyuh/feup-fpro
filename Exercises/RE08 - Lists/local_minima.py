def local_minima(alist, n):
    tup = ()
    alist_prev = alist
    alist_prev += ["n",]*n
    minima = True
    result = ()
    after = False
    count = 0
    resultadofinal = []
    listafinal = []
    for idx, i in enumerate(alist_prev):
        ind = idx - n//2 
        for x in range(n):
            if idx-x < 0 or idx-x > len(alist)-1:
                pass
            else:
                tup = (alist[idx-x],) + tup
                
        if len(tup) <= n//2:
            tup = ()
            continue
        
        while "n" in tup:
            lista_num = list(tup)
            lista_num.pop()
            tup = tuple(lista_num)

        if tup == () or len(tup) <= n//2:
            tup = ()
            continue           
        if len(tup) == n:
            index_value = n//2
            count = 1
            for i in range(n):
                if tup[index_value] > tup[i]:
                    minima = False
            if minima:
                    result += ((tup[index_value], ind),)  
        else:          
            if after:
                count = n//2
                for i in range(len(tup)):
                    if tup[count] > tup[i]:
                        minima = False
                if minima:
                    result += ((tup[count], ind),)                    
            else:
                for i in range(len(tup)):
                    if tup[count] > tup[i]:
                        minima = False
                if minima:
                    result += ((tup[count], ind),)
                count += 1         
        minima = True
        tup = ()
        minimo = list(result)
    for i in minimo:
        if i not in resultadofinal:
            resultadofinal.append(i)
#    if resultadofinal
    for idx, i in enumerate(resultadofinal):
        if idx == 0 or i[1] != resultadofinal[idx-1][1] + 1:
                listafinal.append(i)                
    return listafinal