n = int(input("Escreva o seu número aqui: "))
result = ""

for i in range(n+1):
    if (i % 3) == 0 and (i % 5) == 0:
        result += ""
    elif (i % 3) == 0:
        result += "Fizz" + " "
    elif (i % 5) == 0:
        result += "Buzz" + " "
    else:
        result += str(i) + " "
        
print(result)