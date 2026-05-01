# Check whether any filename appears more than once.
# Print 'Duplicate found' if duplicate exists, otherwise print 'All files are unique'.

# style 1

file_list=[
    'file1.csv',
    'file2.csv',
    'file3.csv',
    'file2.csv'
]

for file in file_list:
    if len(file_list)!=len(set(file_list)):
        print("Duplicate found")
        break
else:
    print("All files are unique")



# style 2

file_list=[
    'file1.csv',
    'file2.csv',
    'file3.csv',
    'file2.csv'
]

seen=set()

for file in file_list:
    if file in seen:
        print('Duplicate found')
        break
    seen.add(file)

else:
    print('All files are unique')



# style 3

file_list=[
    'file1.csv',
    'file2.csv',
    'file3.csv',
    'file2.csv'
]

for file in file_list:
    if file_list.count(file) >1:
        print('Duplicate found')
        break
else:
    print('All files are unique')