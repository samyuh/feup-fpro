def count_exceptions(f, n1, n2):   
    sum = 0
    n3 = n2 + 1   
    for i in range(n1, n3):       
        try:
            f(i)           
        except Exception:
            sum += 1           
    return sum