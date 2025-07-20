import re



email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
egypt_phone_pattern = r'^(010|011|012|015)[0-9]{8}$'
def get_last_user_id():

    with open("data.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            return 0
        last_line = lines[-1]
        try:
            user_id = int(last_line.split(":")[0])
            return user_id
        except:
            return 0
def register ():

    while True :
        fname = input ("Enter your first name : ")
        if  not fname.isalpha():
            print("first name can have only letters")
            continue
        break
    while True :
        lname = input ("Enter your last name : ")
        if not lname.isalpha():
            print("last name can have only letters")
            continue
        break
    while True :
        email = input ("Enter your email : ")
        if not re.match(email_pattern, email) :
            print("Invalid email, please try again")
            continue
        break
    while True :
        password = input ("Enter your password : ")
        if len(password) < 6:
            print("Password must be at least 6 characters")
            continue
        break
    while True :
        confirmed_password = input ("Confirm your password : ")
        if confirmed_password != password:
            print("Passwords don't match, please try again")
            continue
        break
    while True:
        phone = input("Enter your mobile phone number : ")
        if not phone.isdigit():
            print("please enter only numbers")
            continue

        if not re.match(egypt_phone_pattern, phone):
            print("Invalid Egyptian mobile number. please try again")
            continue
        break
    user_id = get_last_user_id() + 1
    with open("data.txt", "a") as fl:
        fl.write(f"{user_id} :  first name:  {fname} , last name:  {lname} , email: {email} , password: {confirmed_password} , phone number: {phone}\n")

    print("\n Congrats! you have registered successfully")

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    found = False
    with open("data.txt", "r") as file:
            for line in file:
                if email in line and password in line:
                    found = True
                    break

    if found:
        print("you have logged in successfully! Welcome back")
        return email
    else:
        print("Invalid email or password. Please try again")
        return 0




