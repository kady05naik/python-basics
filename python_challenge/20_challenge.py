'''
Hollow Right Triangle
'''

def hollow_right_tria(n):
    space=0
    for i in range(1,n+1):
        if i==1 or i==2 or i==n:
            print(f'{"*"*i}')
            
        else:
            space+=1
            print(f'*{" "*space}*')

n=int(input("Enter number:"))
hollow_right_tria(n)