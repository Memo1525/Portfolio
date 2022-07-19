import math
from os import remove
tuplesilla=(123,'John')
print(tuplesilla*2)

print(math.copysign(2 ,-1))

print(33 == 33.0)

#the errors are detected by the python parser 

#Handling Exceptions with Try/Except/Finally 
#We can handle errors by the Try/Except/Finally method. we write unsafe code in the try, fall back code in except and final code in finally block.
#Example 

#logical error don't stop program execution 

# + cannot operate in sets 
# eval , evaluates a string and returns a object 


x = 1
y = 0
assert y != 0, "Invalid Operation" # denominator can't be 0
print(x / y)




s1={1,2,3}
print(s1.remove(1))
print(s1)

d0 = { 'a':1, 'b':2}
d1 = { 'a':3, 'b':4}
d1 > d0

class Demo: 
   def __init__(self,d): 
      self.d=d 
   def print(self): 
      print(self.d)  
a = Demo('Hello') 
a.print()
   
   
   
tuplita=( 'abcd', 786 , 2.23, 'john', 70.2 )

print(tuplita)
# put unsafe operation in try block
try:
     print("code start")
          
     # unsafe operation perform
     print(1 / 0)
  
# if error occur the it goes in except block
except:
     print("an error occurs")
  
# final code in finally block
finally:
     print("GeeksForGeeks")
     