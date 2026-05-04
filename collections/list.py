lst=[[1,2,3],[4,5,6]]
print(type(lst))

# printing second list
print(lst[1])


# Access and read lists
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[2])
print(matrix[2][0])


# Accessing the last element from matrix

print(matrix[-1])
print(matrix[-1][-1])


# Unpacking : List of variables, seperated by commas
person=['Maria',29,'Data Engineer','Spain']
name,age,role,country=person

print("Unpacking...")
print(f'Name: {name}, Age: {age}, Role: {role}, Country: {country}')