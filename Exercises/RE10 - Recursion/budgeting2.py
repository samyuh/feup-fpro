def powerset(l):
    if l == []:
        return [[]]
    x = powerset(l[1:])  
    return x + [[l[0]] + y for y in x]

def budgeting2(budget, products, wishlist):
    lista = []
    buy = []
    save = budget
    bought = {}
    for product in wishlist:
        lista += [product,] * wishlist[product]
    power = list(powerset(lista))
    for i in power:
        if i not in buy:
            buy.append(i)    
    for i in buy:
        price = 0
        budget_control = budget
        for item in i:
            price += products[item]
        budget_control -= price
        if (budget_control < save) and (budget_control) >= 0:
            save = budget_control
            tobuy_list = i
    for i in tobuy_list:
        if i not in bought:
            bought[i] = 1
        elif i in bought:
            bought[i] += 1
    return bought