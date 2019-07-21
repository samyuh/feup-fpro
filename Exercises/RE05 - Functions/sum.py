def sum_numbers(n):
    """
    returns the sum of all positive integers up to and including n
    """
    #### MY CODE STARTS HERE ######################################
    
	sum_num = 0

    
	for i in range(1, n+1):
        
		sum_num += i
    
	return sum_num