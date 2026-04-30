# Check for even number

numbers=[1,3,7,5,1]

for nr in numbers:
    if nr%2==0:
        print(f'{nr} is even from given numbers')
        break
else:
    print('All numbers are odd')