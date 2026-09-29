# CODSOFT INTERNSHIP
# TASK 3 - PASSWORD GENERATOR

import random
import string

print("===================================")
print("       PASSWORD GENERATOR")
print("===================================")

length = int(input("Enter the password length: "))

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
special_characters = string.punctuation

all_characters = lowercase + uppercase + numbers + special_characters

if length < 4:
    print("\nPassword length should be at least 4.")
else:
    password = ''.join(random.choice(all_characters) for _ in range(length))
    print("\nGenerated Password:")
    print(password)

print("\nThank you for using the Password Generator!")
