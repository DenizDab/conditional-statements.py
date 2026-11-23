#phyton program to illustrate the use

# of 'is' identity operator


x=5

if (type(x)is int):#true
   
   print("true") 

else:

   print("false")


x=5.5   

if (type(x)is not float):#false

   print("true")

else:

   print("false")  


x=20

y=20

if (x is  y):#true

   print("x & y same identity")

y=30   

if (x is not y):#true

   print("x & y different identity") 



a = 10

b = -10

# print bitwise right shift operator

print("a >> 1 =", a >> 1)

print("b >> 1 =", b >> 1)


a = 5

b = -10


# print bitwise left shift operator

print("a << 1 =", a << 1)

print("b << 1 =", b << 1) 
      
