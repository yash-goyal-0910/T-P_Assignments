account_profile = {}
acc_id = -1
acc_list = {}
accounts = {}
logged_user = int()
logged = False
def register():
    global acc_id,acc_list,accounts,account_profile,logged_user,logged
    if logged:
        print("Please Log out first")
    usr_nm = input("Enter your Name : ") 
    usr_id = input("Enter your email : ") 
    while usr_id == '0':
        print("Email cant be 0")
        usr_id = input("Enter your email : ") 
    while usr_id in accounts:
        print("User is already preesent, Try different account")
        usr_id = input("Enter your email : ") 
    usr_pass = input("Enter your password : ")
    while usr_pass == '0':
        print("password cant be 0, pls retry")
        usr_pass = input("Enter your password : ")
    usr_age = input("Enter your age : ")
    usr_clg = input("Enter your college : ")
    usr_branch = input("Enter your branch : ")
    usr_year = input("Enter your year : ")
    usr_pass_hash = hash(usr_pass)
    acc_id += 1
    accounts[usr_id] = usr_pass_hash
    acc_list[usr_id] = acc_id
    account_profile[acc_id] = [usr_nm , usr_id , usr_age , usr_clg , usr_branch , usr_year]
    print("Account has been created , please login now")
    login()

def login():
    global logged_user
    global logged
    print("LogIn Page")
    login_usr_id = input("Enter your email : ")
    while login_usr_id not in accounts:
        print("Incoorect Email , enter 0 to quit")
        login_usr_id = input("Enter your email : ")
        if login_usr_id == '0':
            main()
    login_usr_pass = input("Enter your password : ")
    while hash(login_usr_pass) != accounts[login_usr_id]:
        print("Password is incorrect")
        print("enter 0 to quit")
        login_usr_pass = input("Enter your password : ")
        if login_usr_pass == '0':
            main()
    logged_user = acc_list[login_usr_id] 
    logged = True
    print("User is successfully logged in")
    main()
        
def show_profile():
    global logged_user
    global logged
    if logged:
        data = account_profile[logged_user]
        print("Name : " + data[0])
        print("Email : " + data[1])
        print("Age : " + data[2])
        print("College : " + data[3])
        print("Branch : " + data[4])
        print("Year : " + data[5])
        x = input("Press Enter Key To Continue")
        main()
    else:
        print("Log In first please")
        login()

def update_profile():
    global logged_user
    global logged    
    if logged:
        usr_nm = input("Enter your Name : ") 
        usr_id = account_profile[logged_user][1]
        usr_age = input("Enter your age : ")
        usr_clg = input("Enter your college : ")
        usr_branch = input("Enter your branch : ")
        usr_year = input("Enter your year : ")
        account_profile[logged_user] = [usr_nm , usr_id , usr_age , usr_clg , usr_branch , usr_year]
        print("Profile is successfully modified")
        main()
    else:
        print("Log In first please")
        login()
    
def logout():
    global logged_user
    global logged     
    logged = False
    logged_user = None
    print("User is successfully Loged Out")
    main()

def terminate():
    exit()

def main():
    print("Welcome in LNCT")
    response = input('''
        Choose option:
        1. Registration
        2. Login
        3. Profile
        4. Update profile
        5. Logout
        6. Main Menu
        7. Exit

            select option 1/2/3/4/5/6/7: ''')

    if response == '1':
        register()
    elif response == '2':
        login()
    elif response == '3':
        show_profile()
    elif response == '4':
        update_profile()
    elif response == '5':
        logout()
    elif response == '6':
        main()
    elif response == '7':
        terminate()
    else:
        print("Invalid Choice, Please select correct option")
        main()
main()