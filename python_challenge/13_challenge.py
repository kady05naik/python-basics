'''
Pyramid Pattern
'''

def pyramid(n):
    star=1
    space=n-1
    for i in range(1,n+1):
        print(f'{" " * space}{"*" *star}')
        # print(" "*space+"*"*star)
        star=star+2
        space=space-1

n=int(input("Enter a Number to print number:"))
pyramid(n)