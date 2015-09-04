def readNumber(index, text):
	number = ''
	while text[index] != ' ':
		number = number + text[index]
		index = index + 1

	return number,index

fileInput = open('PracticeInput.txt', 'r')
text = fileInput.read()

lines = tuple(open('PracticeInput.txt', 'r'))

m_init = False
counter = 0

num = []
index = 0

one = []
two = []
for line in lines:
	first_matrix = []
	second_matrix = []
	for i in line:

		if i == '|':
			counter = counter+1

		if i.isdigit() or i == '-':
			number, index = readNumber(index,text)
			index = index-1

			if number != '':
				number = float(number)
				if counter/2 == 0:
					first_matrix.append(number)
				else:
					second_matrix.append(number)

		index = index+1

	counter = 0
	one.append(first_matrix)
	two.append(second_matrix)

c = 0
val = 0
output = []

for m2 in xrange(len(two[0])):
	col = []
	for x in one:
		val = 0
		for e in xrange(len(x)):
			
			val = val + x[e]*two[e][c]
		col.append(val)
		
	output.append(col)
	c = c+1	
	
for i in xrange(len(output[0])):
	print "|",
	for r in xrange(len(output)):
		
		print output[r][i],
	print "|"


