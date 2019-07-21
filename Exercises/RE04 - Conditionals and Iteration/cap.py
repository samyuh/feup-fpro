def capicua():
    result = "Not yet implemented"
    num = int(input("Escreva o número: "))

    #Contar o número de digitos do número
    digitos = num
    contador = 0
    while digitos > 0:
        contador += 1
        digitos //= 10
    
    #Obter o capicua
    digitos2 = num
    capicua = 0

    for i in range(contador):
        base_number = digitos2 % 10                     #Obter o número mais à direita
        digitos2 //= 10                                 #Remover o número mais à direita para obter o seguinte no próximo loop
        capicua += (base_number)*(10**(contador-1-i))   #Colocar o número da direita à esquerda, utilizando potencias de 10

    if capicua == num:
        result = str(num) + " is a palidrome."
    else:
        result = str(num) + " is not a palidrome."
    print(result)
    return result

capicua()