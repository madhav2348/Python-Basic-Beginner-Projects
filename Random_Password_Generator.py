import string
import random

character = list(string.ascii_letter + string.digit + "@#$%!&()")

def generate():
    password_len = int("how much long")
    random.shuffle(character)

    password =[]
    
    for x in range(password_len):
    
        password.append(random.choice(character))
    
    random.shuffle(password)
    password = "".join(password)
    
    print(password)

option = input("want to generate password")

if option == "yes" or "YES":
    generate()
elif option == "NO" or "no":
    quit()
else:
    print("invalid")
