
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
       for x in range(1, count):

           if x % dividerf == 0 and x % dividers == 0:
               outstring += ("FB ")

           elif x % dividerf == 0:
               outstring += ("F ")

           elif x % dividers == 0:
               outstring += ("B ")

           else:
               outstring += str(x) + " " 
        
       print(outstring)
   newfile.close()

fizzbuzz(fbfile)


