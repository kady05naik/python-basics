# Whitespace Cleanup

# lstrip(): removes whitespace from left side of the string 
test=" Engineering".lstrip()
print(test)

test="##Engineering".lstrip('#')
print(test)

# rstrip(): removes whitespaces from the right side of the string
test="Engineering ".rstrip()
print(test)

# strip() : removes whitespaces from both the ends
test="  Engineering ".strip()
print(test)

test="####Engineering#".strip('#')
print(test)