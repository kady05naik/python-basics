# 1. Check if the name is not empty 
# and the age is greater than or equal to 18
name="kad"
age=17
print(name != "" and age >=18)


# 2. Check if the password is atleast 8 characters long
# and does not contain spaces
password="kjfksdjfisednf@_12283"
print(len(password)>=8 and " " not in password)


# 3. Check if a user's email is not empty,
# contains '@' 
# and ends with '.com'
email="k@gmail.com"
print(email != '' and '@' in email and '.com' in email)


# 4. Check if a username is a string, 
# is not None, 
# and is longer than 5 characters
username="kadambari"
print(username is not None and isinstance(username, str) and len(username)>5)


# 5. Check if the user is either an admin or moderator, 
# and either they're not banned or they've verified their email
is_admin=True
is_moderator=False
is_banned=True
is_verified= True

print( (bool(is_admin) or bool(is_moderator)) and (is_banned != True or bool(is_verified)) ) 
