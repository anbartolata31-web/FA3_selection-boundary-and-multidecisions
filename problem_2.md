while True:
    password = input("Enter your password: ")
    if 8 <= len(password) <= 15:
        print("Password length is valid.")
        break
    else:
        print("Password too
