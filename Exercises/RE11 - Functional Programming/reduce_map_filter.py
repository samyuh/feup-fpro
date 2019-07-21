from functools import reduce

def reduce_map_filter(args):
    result = []
    if type(args) is list:
        return args
    if type(args) is tuple:
        if args[0] == "map":
            if type(args[2]) is tuple:
                for i in map(args[1], reduce_map_filter(args[2])):
                    result.append(i)
                return result
            else:
                for i in map(args[1], args[2]):
                    result.append(i)
                return result
        if args[0] == "reduce":
            if type(args[2]) is tuple:
                return reduce(args[1], reduce_map_filter(args[2]))
            else:
                return reduce(args[1], args[2])
        if args[0] == "filter":
            if type(args[2]) is tuple:
                for i in filter(args[1], reduce_map_filter(args[2])):
                    result.append(i)
                return result
            else:
                for i in filter(args[1], args[2]):
                    result.append(i)
                return result
        

print(reduce_map_filter(("map", lambda x: 2*x, [1,2,3])) )
print(reduce_map_filter(("reduce", lambda a,b: a+b,("map", lambda x: 2*x,("filter", lambda x: x%2 != 0,[1,2,3])))))