import secrets

import string

letters = string.ascii_letters
digits = string.digits
special_characters = string.punctuation
alphabet = letters + digits + special_characters

print("Welcome to the Password Generator!")

pwd_length = input("How many characters would you like in your password? \n(answer in numerical digits)")
pwd_length = int(pwd_length)
pwd = ' '
for i in range(pwd_length):
    pwd+= ' '.join(secrets.choice(alphabet))

print(pwd)