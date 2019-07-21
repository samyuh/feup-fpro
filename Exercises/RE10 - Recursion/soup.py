def soup(matrix,word):
    for row in range(len(matrix)):
        for letter in range(len(matrix[row])):
            if matrix[row-1][letter-1] == word[0]:
                if vizinho(matrix,row-1,letter-1,word[1:]):
                    return "{}{}".format(chr(ord("A")+row-1),letter)
                
def vizinho(matrix,row,letter,word):
    if word == "":
        return True
    else:
        for r in range(row-1,row+2):
            for l in range(letter-1,letter+2):
                if l>=0 and r>=0 and r<len(matrix) and l<len(matrix) and word[0] == matrix[r][l]:
                    matrix[r][l] == ""
                    if vizinho(matrix,r,l,word[1:]):
                        return vizinho(matrix,r,l,word[1:])