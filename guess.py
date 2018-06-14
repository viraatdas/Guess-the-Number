import random

randy = random.randint(1,10)
a = 0
while a != randy:
  a = input ("guess the number that I am thinking of. Its in between 1 and 10 ")

  if a == randy:
    print "gg"
  else: 
    print "try again"    
  

