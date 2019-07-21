def collisions(alist):
    dictionary = {}
    for number in alist:
        soma = 0
        while number:
            soma += number%10
            number = number//10
        soma_mod = soma % 8
        if soma_mod in dictionary:
            dictionary[soma_mod] += 1
        else:
            dictionary[soma_mod] = 1                 
    return dictionary
            
    
    
print(collisions([1, 789, 100, 9807, 1208, 92, 101]))
