from functools import reduce

def map_reduce(n1, n2):
    '''
    Write a Python function map_reduce(n1, n2) whereby you create a list of the square of the
odd numbers between n1 and n2. Then use reduce to multiply if the accumulated result is
smaller than 50 or add the numbers otherwise. Ensure the result of the function is an integer.
Have a look at reduce() from module functools (Higher-order functions and operations on
callable objects).
'''
    filtrado = filter(lambda x: x % 2 == 1, range(n1, n2+1))
    squares = map(lambda x: x**2, filtrado)
    return reduce(lambda x, y: x*y if x*y<50 else x+y, squares)


print(map_reduce(0, 10))