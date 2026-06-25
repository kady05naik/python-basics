'''
Right Angled Triangle II
'''

def right_ang_tri(n):
    space=n-1
    for i in range(1,n+1):
        print(f'{" "*space}{"*"*i}')
        space-=1

n=int(input("Enter Number:"))
right_ang_tri(n)