'''
Right Angled Triangle with Numbers

'''

def right_angled_triangle_numbers(n):
    for i in range(1,n+1):
        j=str(i)
        print(f'{j*i}')

n=int(input('Enter number:'))
right_angled_triangle_numbers(n)