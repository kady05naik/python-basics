# Allow access only if  the user is logged in 
# Or they are guest
# but they must not be banned

is_logged_in= True
is_guest=False
is_banned=False

print(f"Access Allowed : {(is_logged_in or is_guest) and not is_banned}")