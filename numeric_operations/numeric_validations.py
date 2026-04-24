#  Checks if the float has no decimal part (is whole number)
x=7.0
print(x.is_integer()) # True

x=7.01
print(x.is_integer()) # False

x=7
print(x.is_integer()) # True


# Checks if the value belongs to certain data type ( isinstance(value, type) )
x=70
print(isinstance(x,int)) # True

x=70.99
print(isinstance(x, float)) # True

x='str' 
print(isinstance(x,str)) # True