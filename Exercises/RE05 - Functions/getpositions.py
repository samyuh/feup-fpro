def get_positions(word_list, sentence):
    """
    build the highest possible number out of the combination of 3 digits
    """
    #### MY CODE STARTS HERE ######################################
    
	for i in range(3):
        
		for j in range(3):
            
			if word_list[i] + " " + word_list[j] == sentence:
                
				return str(i) + " " + str(j)