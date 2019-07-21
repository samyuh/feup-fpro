def rec_exceptions(l):   
    result = []    
    for i in l:        
        try:           
           type(i()) == type([])
        except Exception as r:           
                result.append(r)               
        else:
            result += rec_exceptions(i())           
    return result
