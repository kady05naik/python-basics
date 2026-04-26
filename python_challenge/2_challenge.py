# Validate the quality and correctness of Email Values
# - Must not be empty
# - Must contain '.' and '@'
# - Must contain exactly one '@' symbol
# - Must end with '.com', '.org' or '.net'
# - Must not be longer  than 254 characters
# - Must start and end with a letter or digit

email='kady05naik@gmail.com'
if ((email!= '' and '.' in email and '@' in email and email.count('@')==1 and len(email)<256) and (email.endswith('.com') or email.endswith('.org') or email.endswith('.net')) and (email[0].isalpha() or email[0].isnumeric()) and (' ' not in email)):
    print(f"{email} is valid")
else:
    print(f"{email} is not valid")