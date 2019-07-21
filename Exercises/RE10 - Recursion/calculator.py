def calculator(expr):
    if type(expr) is int:
        return expr
    expr = list(expr)
    if type(expr[0]) is tuple:
        expr[0] = calculator(expr[0])
    elif type(expr[2]) is tuple:
        expr[2] = calculator(expr[2])  

    if expr[1] == '+':
        result = expr[0] + expr[2]
    elif expr[1] == '-':
        result = expr[0] - expr[2]
    elif expr[1] == '*':
        result = expr[0] * expr[2]
    return result
        
    
    
    
