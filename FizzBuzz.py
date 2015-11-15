
#Michael Zazula

import sys
fbfile = system.argsv[1 ]

def fizzbuzz(file):
   newfile = open(file, "r")
   outList = []

   for line in newfile:
       
       print(newfile)
       line = line.split()

       if len(line)<= 1:
       	break
       # first divider
       dividerf = int(line[0])

       # second divider
       dividers = int(line[1])

       # how many times this will run
       count = int(line[2])

       for x in range(1, count + 1):

           if x % dividerf == 0 and x % dividers == 0:
               outList.append("FB")

           elif x % dividerf == 0:
               outList.append("F")

           elif x % dividers == 0:
               outList.append("B")

           else:
               outList.append(x)
       return outList
   newfile.close()

fizzbuzz(fbfile)


