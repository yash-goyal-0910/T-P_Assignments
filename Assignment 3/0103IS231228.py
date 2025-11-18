import json
import random
import datetime

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
        x = input("Press Enter Key To Continue")
        main()
        return
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

def take_ans():
    ans = input("Choose option a/b/c/d : ")
    if ans.upper() not in ['A','B','C','D']:
        print("Invalid Option -")
        take_ans()
    return ans.upper()

def show_ques(topic):
    global account_profile
    global logged_user
    topics = ['DSA','DBMS','PYTHON']
    def load_ques(topic):
        file_mapping = {
            1: 'dsa_questions.json',
            2: 'dbms_questions.json', 
            3: 'python_questions.json'
        }
        
        with open(file_mapping[topic], 'r') as f:
            return json.load(f)
    questions = load_ques(topic)
    random.shuffle(questions)
    score = 0
    for i,ques in enumerate(questions):
        print(f'{i+1}. ' + ques['question'])
        for option in ques['options']:
            print('  ' + option)
        ans = take_ans()
        if ans == ques['correct']:
            score += 1
    account_profile[logged_user].append(topics[topic-1]) # this has a flaw in case where single person who has given multiple quiz
    account_profile[logged_user].append(score)
    x = datetime.datetime.now()
    account_profile[logged_user].append(str(x)[0:19])
    print("Quiz successfully submitted , score = " ,score)
    x = input("Press Enter Key To Continue")
    main()

def Quiz():
    global logged_user
    global logged
    if logged:   
        response = input('''
        Choose Topic:
        1. DSA
        2. DBMS
        3. PYTHON

            Press 4 to Return
            select option 1/2/3/4: ''')
        if response in ['1','2','3','4']:
            if response == '4':
                main()
            show_ques(int(response))
        else:
            print("Invalid Choice, Please select correct option")
            Quiz()
    else:
        print("Log In first please")
        login()
        
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

def score():
    print("Score Table :")
    print('Name'.ljust(12)+'Topic'.ljust(8)+'Marks'.ljust(8)+'date/time'.ljust(19))
    for i in range(1,len(account_profile)):
        account_info = account_profile[i]
        print(account_info[0].ljust(12)+account_info[6].ljust(8)+f'{account_info[7]}/10'.ljust(8)+account_info[8].ljust(19))
    x = input("Press Enter Key To Continue")
    main()    


def main():
    global logged
    global logged_user
    if logged_user == 0 and logged:
        print("Welcome in LNCT")
        response = input('''
        Choose option:
        1. Score
        2. Logout
        3. Exit

            select option 1/2/3: ''')
        
        if response == '1':
            score()
        elif response == '2':
            logout()
        elif response == '3':
            terminate()
        else:
            print("Invalid Choice, Please select correct option")
            main()
    else:
        print("Welcome in LNCT")
        response = input('''
            Choose option:
            1. Registration
            2. Login
            3. Profile
            4. Update profile
            5. Logout
            6. Quiz
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
            Quiz()
        elif response == '7':
            terminate()
        else:
            print("Invalid Choice, Please select correct option")
            main()

def create_admin():
    global acc_id,acc_list,accounts,account_profile,logged_user,logged
    usr_nm = 'admin'
    usr_id = 'admin'
    usr_pass = 'admin'
    usr_age = 'admin'
    usr_clg = 'admin'
    usr_branch = 'admin'
    usr_year = 'admin'
    usr_pass_hash = hash(usr_pass)
    acc_id += 1
    accounts[usr_id] = usr_pass_hash
    acc_list[usr_id] = acc_id
    account_profile[acc_id] = [usr_nm , usr_id , usr_age , usr_clg , usr_branch , usr_year]

def create_ran_user():
    global acc_id,acc_list,accounts,account_profile,logged_user,logged
    usr_nm = '1'
    usr_id = '1'
    usr_pass = '1'
    usr_age = '1'
    usr_clg = '1'
    usr_branch = '1'
    usr_year = '1'
    usr_pass_hash = hash(usr_pass)
    acc_id += 1
    accounts[usr_id] = usr_pass_hash
    acc_list[usr_id] = acc_id
    account_profile[acc_id] = [usr_nm , usr_id , usr_age , usr_clg , usr_branch , usr_year]

create_admin()
create_ran_user()
main()