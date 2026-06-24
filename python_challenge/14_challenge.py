'''
Inverted Pyramid Pattern

'''

def inverted_pyramid(n):
    space=0
    star=(n*2)-1
    for i in range(n):
        print(f'{" "*space}{"*"*star}')
        space=space+1
        star=star-2

n=int(input('Enter number:'))
inverted_pyramid(n)