'''
Hollow Square of side 'N'
'''

def halsqr(n):
    for i in range(n):
        if i==0 or i==n-1:
            print("* "*n)
        else:
            for j in range(n):
                if j not in(0,n-1):
                    print(" ", end =" ")
                else:
                    print("*",end=' ')
            print()
            
n=int(input("Enter a number:"))
halsqr(n)