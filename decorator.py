import functools
def arith_operation(func):
    @functools.wraps(func)  # Keep the original function name & docstring
    def arithematic(*args, **kwargs):   # Accepts any number of arguments
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(result)
        print("************--------------------*****************************-------------------***************")
        return result
    return arithematic
@arith_operation
def add(a, b):
    print("Addition of two numbers :->")
    return 'The addition of',a ,'+', b,'=',a + b
add(102,34)

@arith_operation
def addthree(a, b, c):
    print("Addition of three numbers :->")
    return 'The addition of',a ,'+', b, '+',c ,'=',a + b + c
addthree(10, 20, 30)

@arith_operation
def sub(a , b):
    print("Subtraction of two numbers :->")
    return 'The subtraction of',a ,'-', b,'=',a - b
sub(76, 23)

@arith_operation
def mult(a, b):
    print("Multiplication of two numbers :->")
    return 'The multiplication of',a ,'*', b,'=',a * b
mult(45, 8)

@arith_operation
def div(a, b):
    if b == 0:
        print("Can't divide by zero")
    else:
        print("Division of :->")
    return a, "/", b, "=", a/b
div(13, 2)

@arith_operation

def greet(a):
    return a
greet("Hey Rachana")

'''
OUTPUT :->
Calling function: add
Addition of two numbers :->
('The addition of', 102, '+', 34, '=', 136)
************--------------------*****************************-------------------***************
Calling function: addthree
Addition of three numbers :->
('The addition of', 10, '+', 20, '+', 30, '=', 60)
************--------------------*****************************-------------------***************
Calling function: sub
Subtraction of two numbers :->
('The subtraction of', 76, '-', 23, '=', 53)
************--------------------*****************************-------------------***************
Calling function: mult
Multiplication of two numbers :->
('The multiplication of', 45, '*', 8, '=', 360)
************--------------------*****************************-------------------***************
Calling function: div
Division of :->
(13, '/', 2, '=', 6.5)
************--------------------*****************************-------------------***************
Calling function: greet
Hey Rachana
************--------------------*****************************-------------------***************
'''


