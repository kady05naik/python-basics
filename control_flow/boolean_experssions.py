# bool(value) =>True 
# True  => if the value is non-empty or non-zero
# False => if the value is empty or zero

print(True)         # True
print(False)        # False
print(type(True))   # <class 'bool'> 
print(bool(123))    # True
print(bool("Hi"))   # True
print(bool())       # False
print(bool(0))      # False
print(bool(""))     # False
print(bool(None))   # False