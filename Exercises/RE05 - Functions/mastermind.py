def mastermind(g1, g2, g3, c1, c2, c3):
    """
    evaluate a line of the mastermind game
    """
    #### MY CODE STARTS HERE ######################################
    
	points = 0
    
	if g1 == c1:
        
		points += 3
    
	elif g1 == c2 or g1 == c3:
        
		points += 1
  
 
	if g2 == c2:
        
		points += 3
    
	elif g2 == c1 or g2 == c3:
        
		points += 1

  
  
	if g3 == c3:
        
		points += 3
    
	elif g3 == c1 or g3 == c2:
        
		points += 1
        
    
	return points