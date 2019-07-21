def raise_exception(alist, value):    
    result = []
    for i in alist:
        if i <= value:
            result.append(ValueError("{} is not greater than {}".format(i, value)))
    return result