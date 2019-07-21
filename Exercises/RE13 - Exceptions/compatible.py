def compatible(A, B):    
    a_len = len(A[0])
    b_len = len(B)    
    try:
        assert a_len == b_len
    except AssertionError:        
        return AssertionError("A and B cannot be multiplied")        
    else:
        return "A and B can be multiplied"