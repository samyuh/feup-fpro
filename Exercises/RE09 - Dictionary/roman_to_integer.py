def roman_to_integer(astring):
    roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    next_int = roman_int[astring[1]]
    total = 0
    for idx, roman in enumerate(astring):
        if roman in roman_int:
            inteiro = roman_int[roman]
            if inteiro >= next_int:
                total += inteiro
            else:
                total -= inteiro                
            if idx >= len(astring)-2:
                next_int = 0
            else:
                next_int = roman_int[astring[idx+2]]
    return total