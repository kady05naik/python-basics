'''
Number of Rounds of Lift

'''
import math

def calculate_lift_rounds(n, capacity):
    return math.ceil(n/capacity)

n=int(input('Enter total number of people: '))
capacity=int(input('Enter the maximum number of people: '))

print(f'Number of Rounds of Lift: {calculate_lift_rounds(n, capacity)}')