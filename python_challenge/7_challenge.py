# while loop
# ALlow up to 3 attempts
# If the user types 'yes', print 'Glad we are on the same page'
# Otherwise, print '3 Strikes, You are out!'

i=0
while i<3:
    if input('Are we on the same page(yes/no)?') !='yes':
        i=i+1
    else:
        print('Glad we are on the same page')
        break
else:
    print('3 Strikes, You are out!')