'''
Celsius to Fahrenheit
'''

def celsius_to_fahrenheit(c):
    f = (9/5 * c) + 32
    return f

c=int(input(f'Enter temperature in celcius: '))
print(celsius_to_fahrenheit(c))