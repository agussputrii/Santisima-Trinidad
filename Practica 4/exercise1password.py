saved_pass = "elpepe"

for i in range(3):
    password = input("Enter the password: ")
    if password == saved_pass:
        print("¡Welcome User!")
        break
    else:
        print("Incorrect password!")
        continue