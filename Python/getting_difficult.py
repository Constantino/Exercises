from sys import argv 
import random

def is_prime(n):
	if n <= 1:
		return False
	else:
	    i = 2
	    while i < n:
	        if n%i == 0:
	            return False
	        i += 1
    	return True

m = int(argv[1])
n = int(argv[2])

array = [[random.randint(0,100) for e in range(n)] for e in range(m)]

prime_numbers = []

for x in range(len(array)):
	for y in range(len(array[x])):
		print "Position: ",x,",",y," value: ",array[x][y]
		if is_prime(array[x][y]) and array[x][y] not in prime_numbers:
			prime_numbers.append(array[x][y])

print "\nprime_numbers: ",prime_numbers

