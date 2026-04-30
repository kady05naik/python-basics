# Print a left -aligned pyramid of stars with 6 rows using a for loop
# *
# **
# ***
# ****
# *****
# ******


# style 1
for i in range (1,7):
    print(f"{"*"*i}")


# style 2
for i in range (7):
    print()
    for j in range (i):
        print("*", end="")