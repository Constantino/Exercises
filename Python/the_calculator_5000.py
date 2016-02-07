def get_numbers():
	List = []

	while True:
		
		try:
			number = raw_input("Type a number or 'q' to quit: ")
			
			if number == "q":
				break

			number = float(number)
			List.append(number)
			
		except ValueError:
			
			print "That's not a number!"

	return List

def product(List):
	result = 1
	for e in List:
		result *= e
	return result
	
List = get_numbers()
print "\nSum: ",sum(List)
print "product: ",product(List)
