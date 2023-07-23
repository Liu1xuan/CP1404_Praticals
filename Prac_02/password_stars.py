MINIMUM = 7


def main():
    password = get_password()
    print(len(password)*"*")


def get_password():
    password = str(input("Password: "))
    while len(password) < MINIMUM:
        print("Invalid and your password at least 7 characters.")
        password = str(input("Password: "))
    else:
        return password


main()










