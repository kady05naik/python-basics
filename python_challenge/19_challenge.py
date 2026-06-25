'''
Sandglass Pattern
'''

def sand_glass(n):
    space=-1
    star=(n*2)+1
    for i in range(n):
        space=space+1
        star=star-2
        print(f'{"  "*space}{"* "*star}')
    
    for i in range(n-1):
        space=space-1
        star=star+2
        print(f'{"  "*space}{"* "*star}')


n=int(input("Enter number:"))
sand_glass(n)