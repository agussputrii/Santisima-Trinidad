import re

def main():
    password = input("Enter your password: ")
    reg = ("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")

    pat = re.compile(reg)

    mat = re.search(pat, password)

    if mat:
        print("Password is valid, welcome!")
    else:
        print("PASSWORD IS NOT VALID!")

if __name__ == "__main__":
    main()