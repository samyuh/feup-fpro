def cut(filename, delimiter, field):
    with open(filename, "r") as f:
        lista = []
        result =[]
        f = f.read()
        f = f.split("\n")
        for line in f:
            lista.append(line.split(delimiter))
  
        if type(field) is list:
            temp1 = []
            for line in lista:
                temp = []
                for i in field:
                    if len(line) >= i:
                        temp.append(line[i-1])
                temp1 += [temp,]
            for i in temp1:
                result += [delimiter.join(i),]
        else:
            for line in lista:
                if len(line) >= field:
                    result.append(line[field-1])
        return "\n".join(result)

print(10 < 2)