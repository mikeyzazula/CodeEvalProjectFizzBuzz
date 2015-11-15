#Michael Zazula 
#Codeeval FizzBuzz

import sys 

def fizzbuzz(file):
	test_file = open(file,r)
	outList =[]
	
	for line in file:
	

		#first divider 
		dividerf = line[0]

		#second divider
		dividers = line[1]
		
		#how many times this will run 	
		count = line[2]

		

		for x in range(1,count+1):
			
			if x%dividerf == 0 and x%dividers == 0:
				outList.append("FB")

			elif x%dividerf == 0:
				outList.append("F")

			elif x%dividers == 0:
				outList.append("B")

			else:
				outList.append(x)
		return outList
	
fizzbuzz(args[v1])

