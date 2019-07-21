
def concatenate():
    
	result = "Not yet implemented"
    
	n1 = int(input("Escreva o primeiro número: "))
    
	n2 = int(input("Escreva o segundo número: "))

 
   
	i = n2
    
	expoente = 0
   

	while i > 0:
        
		expoente += 1
        
		i //= 10 

    
	result = n1*(10**expoente) + n2
    return result