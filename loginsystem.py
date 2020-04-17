def register():
    create_user=input("Type in preferred username:")
    file_create=open("//home/kaysha/Documents/MS-Python-Pre-work/my_passwords/users/"+create_user,"w")
    create_pass=input("Type in preferred password:")
    file_create.write(create_pass)
    file_create.close()
def login():
    repeat_main=True
    while repeat_main:
        username= input("Input Username: ")
        try:
            user=open("//home/kaysha/Documents/MS-Python-Pre-work/my_passwords/users/"+username, "r")
            password=input("Input Password: ")
            if password in user:
                repeat_main=False
                user.close()
            else:
                print("Invalid Password!")
        except:
            print("User Not Found!")
    print("Login Successful!")
reglog=input("Login or Register new account? ").title()
if reglog=="Register":
    register()
elif reglog=="Login":
    login()
else:
    exit()