
#Michael Zazula

import sys
fbfile = sys.argv[1]

def fizzbuzz(file):
	newfile = open(file, "r")


	for line in newfile:

		line = line.split()

		if len(line)<= 1:
			break
		# first divider
		dividerf = int(line[0])

		# second divider
		dividers = int(line[1])

		# how far this will count
		count = int(line[2])
		outstring = ""
		#For everything EXCEPT the last character we need a space
		for x in range(1, count+1):

			if x % dividerf == 0 and x % dividers == 0:
				outstring += ("FB ")

			elif x % dividerf == 0:
				outstring += ("F ")

			elif x % dividers == 0:
				outstring += ("B ")

			else:
				outstring += str(x) + " "
			#To avoid trailing white space, for the last character we have to remove that last space
		outstring = outstring[:-1]
		print(outstring)
	newfile.close()

fizzbuzz(fbfile)


