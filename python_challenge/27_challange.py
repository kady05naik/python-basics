'''
Line Equation

'''

def calculate_y(slope, intercept, x):
    return (slope*x+intercept)


slope=float(input('Enter slope: '))
intercept=float(input('Enter intercept: '))
x=float(input('Enter x: '))

print(f'Line Equation: {calculate_y(slope, intercept, x)}')