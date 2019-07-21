def is_perfect(n):
    """
    check whether a number n is perfect 
    """
    #### MY CODE STARTS HERE ######################################
    
	sum_div = 0

    
	for i in range(1, n):
        
		if (n % i) == 0:
            
			sum_div += i

    
	if sum_div == n:
        
		return True
    
	else:
        
		return False