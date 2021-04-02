# Program that will ask the user how many Fibonacci numbers to generate and then generate them.  
# : 1, 1, 2, 3, 5, 8, 13,…) // the first two are 1
#**: Function asks for a number in the Fibonacci sequence and gives you a list of those numbers


def fibo(nu):

    x = 1  

    if nu == 0:
        fib = []

    elif nu == 1:
        fib = [1]

    elif nu ==2:
        fib = [1,1]
    elif nu > 2:
        fib = [1,1]
        while x < (nu -1):
            fib.append(fib[x] + fib[x-1])
            x = x +1

    print(fib)


# fibo(457453) <- try this

