'''
Inverted Right Angled Triangle
'''
def inv_right_angled_triangle(n):
    for i in range(n,0,-1):
        print("* "*i)

n=int(input("Enter number:"))
inv_right_angled_triangle(n)