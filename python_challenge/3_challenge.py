# Validate the quality and correctness of passwords
# - Must not be empty
# - Must be atleast 8 characters
# - Must include at least 1 uppercase 
# - Must include at least 1 lowercase
# - Must not be same as the email
# - Must not contain any spaces
# - Must start and end with a letter or digit

email='kady05naik@gmail.com'
password='ksjdksdfjkhdkjfh7617w6716F'
if password == '':
    # - Must not be empty
    print("Password should not be empty")

elif len(password)<8:
    # - Must be atleast 8 characters
    print("Password length should be at least 8")

elif not any(char.isupper() for char in password):
    # - Must include at least 1 uppercase 
    print(f"{password} must include at least 1 uppercase ")

elif not any(char.islower() for char in password):
    # - Must include at least 1 lowercase
    print(f"{password} must include at least 1 lowercase")

elif password==email:
    # - Must not be same as the email
    print(f"{password} must not be same as the email ")

elif ' ' in password :
    # - Must not contain any spaces 
    print(f"{password} must not contain any spaces ")

elif not (password[0].isalnum() and password[-1].isalnum()):
    # - Must start and end with a letter or digit
    print(f"{password} must start and end with a letter or digit ")

else:
    print(f'{password} is valid')