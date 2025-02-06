import random

def generate_passwords():
    print("\nGenerate Random Password")
    randomchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&"

    nbrofpwds = int(input("Please enter the number of passwords to be generated: "))

    # Ensure password length is at least 6
    while True:
        pwdlen = int(input("Please enter the length of the password needed (must be >= 6): "))
        if pwdlen >= 6:
            break
        print("Password length must be at least 6 characters. Please try again.")

    print("\nHere are your random passwords:")
    for x in range(nbrofpwds):
        pwd = ""
        for chars in range(pwdlen):
            pwd = pwd + random.choice(randomchars)
        print(pwd)

def front_page():
    while True:
        print("\nGenerate Random Password!")
        print("1. Generate Passwords")
        print("2. Exit")
        choice = input("Please select an option (1 or 2): ")

        if choice == '1':
            generate_passwords()
    
        elif choice == '2':
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the front page
front_page()
