'''
Number Pyramid Pattern
'''

def num_pyramid(n):
    space=n
    count=1
    for i in range(1,n+1):
        space=space-1
        print(f'{"  "*space}', end='')

        for j in range(1,i+count):
            print(f'{j}',end=' ')
        print()
        count+=1
        

n=int(input("enter number:"))
num_pyramid(n)

