#   Print 7 table from 1 to 10 using a for loop

# style 1
for i in range(1 , 11):
    print(f"7 * {i} = {7 * i}")


# style 2
j=1
for i in range(7,71,7):
    print(f"7 * {j} = {i}")
    j=j+1


#style 3
val=7
ans=0
for i in range(1,11):
    ans=val*i
    print(f"7 * {i} = {ans}")
