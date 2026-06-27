'''
Distance covered by a Vehicle
'''

def calculate_distance(speed, time):
    return speed*time

speed=int(input('Enter speed: '))
time=int(input('Enter time: '))

print(f'Distance covered by a Vehicle: {calculate_distance(speed, time)}')