def parse(filename):
    result = ""
    with open(filename, "r") as f:
        lines = f.readlines()
        for linha in lines:
            words = linha.split()
            for word in words:
                if word == "(":
                    result += "("
                else:
                    result += word + ","
    result = "("+result+")"
    return eval(result)
