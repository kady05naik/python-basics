'''
Diamond Pattern
'''

def diamond(n):
    star=1
    space=n-1
    for i in range(1,n+1):
        print(f'{"  " * space}{star * "* "}')
        star=star+2
        space=space-1
    
    star=star-4
    space=1
  
    for i in range (n,1,-1):
        print(f'{"  " * space}{"* " * star}')
        star=star-2
        space=space+1

n=int(input("Enter Number:"))
diamond(n)