'''
Rectangle Pattern
'''
def rec(row,col):
    for i in range(row):
        print("* "*col)

r=int(input("Number of rows:"))
c=int(input("Number of columns:"))
rec(r,c)