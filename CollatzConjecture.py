import sys

#Set the recursion limit high enough so that the interations isn't a problem
sys.setrecursionlimit(3000)

#Initialize the list of previously found values. This is so that we know if we hit a loop and therefore solved the conjecture.
values_list = []

def calculate(value):
	index = 1
	while True:
		#See if we already had the value before. If so, the print the conjecture has been solved. If not the added it and keep calculating
		if value not in values_list:
			values_list.append(value)
		else:
			print ('Solved!')
			return

		#If the value is even, divide it by 2. If the value is odd, multiple it by 3 and add 1.
		if value % 2 == 0:
			value = value / 2
		else:
			value = (3 * value) + 1

			#Print the iteration this is and the value at this interation.
		print ('Iteration '+ str(index) + ': '+ str(int(value)))
			#If value is equal to 1, then the starting value didn't disprove the conjecture.
		if value == 1:
			print('\nIterations: ' + str(index))
			break
		index = index + 1


def sanatizeArg(arg):
	return 2
calculate(int(sys.argv[1]))
