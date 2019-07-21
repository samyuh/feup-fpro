def palindrome(astring):
    number = len(astring)
    count = 0
    for k in range(number):
        for i in range(2+k, number+1):              
                result = astring[k:i]
                if result == result[::-1]:
                    count += 1
    result = "For string" + " '" + astring + "':" + " " + str(count) + " " + "palindrome substrings"
    return result