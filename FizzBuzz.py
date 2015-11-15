#Michael Zazula 
#Codeeval FizzBuzz


#print "Input a file"
#num_file = open("input.txt", "r")


#first divider 
dividerf = 3
#second divider
dividers = 5
#how many times this will run 
count = 10


for x in range(1,count):
	
	if x%dividerf == 0 && x%dividers == 0:
		print "FB"

	elif x%dividerf == 0:
		print "F"

	elif x%dividers == 0:
		print "B" 

	else:
		print "count"
		