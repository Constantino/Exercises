from sys import argv 

def factorial(n):

    return 1 if n<=0 else n*factorial(n-1)

for i in range(1,int(argv[1])+1):
	print factorial(i)