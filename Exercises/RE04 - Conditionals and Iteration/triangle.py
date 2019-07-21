lado1 = int(input("Escreva o primeiro lado do triângulo: "))
lado2 = int(input("Escreva o segundo lado do triângulo: "))
lado3 = int(input("Escreva o terceiro lado do triângulo: "))

#Verificar se é triângulo
#lado1 < lado2 + lado3
#lado2 < lado1 + lado3
#lado3 < lado1 + lado2

if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2) == True:
    if (lado1 != lado2 != lado3) == True:
        print("Scalene")
    elif (lado1 == lado2 == lado3) == True:
        print("Equilateral")
    else:
        print("Isosceles")
else: 
    print("Not a Triangle")
    