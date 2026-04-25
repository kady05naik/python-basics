x=10
y=10
print(x is y)   # True
# This is optimization instead of creating seperate objects x and y 
# python points x, y to the same object in integer pool


x=[1,2,3]
y=x
print(x is y)   #True
# while creating y=x you are not creating new list 
# you are asking python to point y 
# to the same object that x currently pointing


x=[1,2,3]
y=[1,2,3]
print(x==y)     # True
print(x is y)   # False
# When you create list with [] python allocates new block of memory
# even though values inside are identical x, y are two different objects
