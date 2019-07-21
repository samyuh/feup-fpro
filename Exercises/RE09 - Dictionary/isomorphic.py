def isomorphic(astring1, astring2):
    maping = {}
    palavra2 = ""
    for idx, letter in enumerate(astring1):
        if letter not in maping:
            maping[letter] = astring2[idx]
        palavra2 += maping[letter]        
    valores = maping.values()
    if palavra2 == astring2 and len(set(valores)) == len(valores):    
        return "'{}' and '{}' are isomorphic because we can map: {}".format(astring1, astring2, list(maping.items()))
    else:
        return "'{}' and '{}' are not isomorphic".format(astring1, astring2)