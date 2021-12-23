import os
import time
from datetime import datetime
listcommands = [
    "help",
    "datetime",
    "about",
    "username",
    "clear",
    "adduser",
    "logout",
    "shutdown",
    "restart"
    ]
cmdlist = '\n'.join(listcommands)
userfile = "user.txt"
datetimenow = datetime.now()
datetimeinput = datetimenow.strftime("%B %d, %Y %H:%M")
def username_set():
    os.system("cls")
    check_userfile = os.path.isfile(userfile)
    if check_userfile == True:
        login()
    else:
        create_user()

def create_user():
    file_register = os.path.isfile(userfile)
    if file_register == True:
        with open(userfile, "r") as user_name:
            file_set = user_name.read()
            user_name_list = file_set.split()
        os.system("cls")
        user = input("Please enter your username to call in shell: ")
        if user in user_name_list:
            print("This username been taken. Please take the difference name.")
            os.system("pause")
            create_user()
        else:
            with open(userfile, "a") as write_sys:
                write_sys.writelines([user, "\n"])
            username_set()
    if file_register == False:
        os.system("cls")
        user = input("Please enter your username to call in shell: ")
        with open(userfile, "a") as write_sys:
            write_sys.writelines([user, "\n"])
        username_set()


def login():
    global user_print
    os.system("cls")
    with open(userfile, "r") as check_login_file:
        file_content = check_login_file.read()
        user_list = file_content.split()
    userinput = input("Please enter your username: ")
    if userinput in user_list:
        user_print = userinput
        shell()
    else:
        print("User not found!")
        os.system("pause")
        login()
def shell():
    os.system("cls")
    print("Hello " + str(user_print) + "!")
    print("The date and time now is: " + str(datetimeinput))
    print("""Type "help" to open help""")
    prompt()

def prompt():
    shell = input("main~$: ")
    if shell in listcommands:
        if shell == "help":
            help()
        if shell == "datetime":
            print("The date and time now is: " + str(datetimeinput))
            prompt()
        if shell == "about":
            about()
        if shell == "clear":
            os.system("cls")
            prompt()
        if shell == "username":
            print("Your username is " + str(user_print))
            prompt()
        if shell == "adduser":
            print("This will log you out!")
            logout = input("Are you sure? (y/n): ")
            if logout == "y":
                create_user()
            else:
                prompt()
        if shell == "logout":
            confirm = input("Are you sure? (y/n): ")
            if confirm == "y":
                login()
            else:
                prompt()
        if shell == "shutdown":
            print("Shutting down...")
            time.sleep(2)
            safeshutdown()
        if shell == "restart":
            print("Restarting...")
            time.sleep(2)
            boot()
    else:
        if shell == "":
            prompt()
        print("Unkhown command!")
        print("""Type "help" to open help""")
        prompt()


def about():
    print("Shell Command in Python - Made by Dinh Huy")
    print("Still on development.")
    prompt()

def help():
    print("This is all commands in shell")
    print(cmdlist)
    prompt()

def boot():
    print_progress = 0
    while print_progress != 100:
        time.sleep(0.01)
        os.system("cls")
        print("[" + "*" * print_progress +"]")
        print("Progress: " + str(print_progress) + "%")
        print_progress += 1
    username_set()


def safeshutdown():
    os.system("cls")
    print("""
    -----------------------------------------------------



                If safe to close the shell.



    -----------------------------------------------------
    """)
    input()
    quit()


boot()