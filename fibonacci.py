def recursiveFibonacci(num):
#0 is the zeroth position in the series
    if num == 0 or  num == 1:
        return num
    else:
        return recursiveFibonacci(num - 2) + recursiveFibonacci(num - 1)

def fibonnacciSeries(num):
    a, b, index  = 0, 1, 0
    while index <= num:
        print(a, end=',')
        a, b = b, a+b
        index =  index + 1

def fib(num):
    a, b = 0, 1
    while a <= num:
        print(a, end=',')
        a, b = b, a+b

#Test Fibonacci
print(recursiveFibonacci(8))
print(fibonnacciSeries(8))
#fib(8)



