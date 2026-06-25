'''
Hollow Inverted Right Triangle
'''

def inverted_right_angled_triangle(n):
    space=n-3
    for i in range(n,0,-1):
        if i == 1 or i==2 or i==n:
            print("*"*i)

        else:
            print(f'{"*"}{" "*space}{"*"}')
            space-=1

n=int(input("Enter Number: "))
inverted_right_angled_triangle(n)

