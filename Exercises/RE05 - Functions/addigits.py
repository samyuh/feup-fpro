def adigits(n1, n2, n3):
    
"""
    build the highest possible number out of the combination of 3 digits
    """
    
#### MY CODE STARTS HERE ######################################
    
	n1 = int(n1)
    
	n2 = int(n2)
    
	n3 = int(n3)
    
	if n1 >= n2 >= n3:
        
		n = n1*100 + n2*10 + n3
        
		return n
    
	elif n1 >= n3 >= n2:
         
		n = n1*100 + n3*10 + n2
         
		return n
    
	elif n2 >= n3 >= n1:
         
		n = n2*100 + n3*10 + n1
         
		return n
    
	elif n2 >= n1 >= n3:
         
		n = n2*100 + n1*10 + n3
         
		return n
    
	elif n3 >= n1 >= n2:
         
		n = n3*100 + n1*10 + n2
         
		return n
    
	elif n3 >= n2 >= n1:
         
		n = n3*100 + n2*10 + n1
         
		return n