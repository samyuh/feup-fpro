def budgeting(budget, products, wishlist):
    compras = {}
    products = dict(sorted(products.items(), key=lambda x: x[1], reverse = True))
    for item in products:
        if item in wishlist:
            quantidade = wishlist[item]
            for _ in range(quantidade):
                pagar = products[item]
                budget -= pagar
                if budget < 0:
                    return compras
                elif item not in compras:
                    compras[item] = 1
                else:
                    compras[item] += 1
    return compras