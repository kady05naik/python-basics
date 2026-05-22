person=['Maria',29,'Data Engineer','Spain']
name,_,role,city=person
print(name,role,city)


person=['Maria',29,'Data Engineer','Spain']
name,*_,city=person
print(name,city)