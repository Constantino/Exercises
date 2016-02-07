from sys import argv 

def quick_sort(List):
   if len(List) > 1:
     pivot = len(List)/2
     numbers = List[:pivot]+List[pivot+1:]
     left  = [e for e in numbers if e < List[pivot]] 
     right =[e for e in numbers if e >= List[pivot]]
     return quick_sort(left)+[List[pivot]]+quick_sort(right)
   return List

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

List = get_numbers()

print "\nNumbers_list: ", List

sorted_list = quick_sort(List)

print "sorted_list: ", sorted_list

print "\nHighest number: ", sorted_list[-1]
print "lowest number: ", sorted_list[0]

