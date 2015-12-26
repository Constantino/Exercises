from sys import argv 

def factorial(n):

    return 1 if n<=0 else n*factorial(n-1)

print factorial(int(argv[1]))
