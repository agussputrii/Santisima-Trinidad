def password_valid(password):

    special_sym = ['@','-','%','/','&']
    complete_val = True

    #password legth check
    if len(password) > 20:
        print("Password must be less than 20 characters")
        complete_val = False

    if len(password) < 6:
        print("Password must be at least 6 characters")
        complete_val = False

    #password chars check: NUMBERS
    if not any(char.isdigit() for char in password):
        print("Password should have at least one numeral")
        complete_val = False

    #PASSWORD chars check: UPPERCASE
    if not any(char.isupper() for char in password):
        print("Password should have at least one uppercase letter")
        complete_val = False

    #password char check: SPECIAL CHARACTERS
    if not any(char in special_sym for char in password):
        print("Password should have at least one of the special characters: '@','-','%','/','&'")
        complete_val = False

    if complete_val:
        return complete_val


def main():
    password = input("Enter your new password: ")

    for i in range(2):
        if password_valid(password):
            print ("Password is correct!")
            break
        else:
            print("PASSWORD IS NOT CORRECT!")
            password = input("Enter your new password: ")

if __name__ == '__main__': 
    main() 