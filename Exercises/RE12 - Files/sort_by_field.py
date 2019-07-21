def sort_by_field(filename, field):
    with open(filename, "r") as emails:
        emails = emails.read()
        emails = emails.split("\n")
        lista = []
        for idx, info in enumerate(emails):
            if idx == 0:
                result = [info,]
                info = info.split(",")
                number = info.index(field)
            else:
                info = info.split(",")
                lista.append(info)
        lista_sort = sorted(lista, key= lambda x: x[number])
        for i in lista_sort:
            result += [",".join(i),]
        return "\n".join(result)