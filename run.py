#!/usr/bin/env python3.6
import random
from credential import Credential
from user import User


##credential 
def create_credential(fname,lname,uname,pnumber,email,password):
    '''
    Function to create new credentials
    '''
    new_credential = Credential(fname,lname,uname,pnumber,email,password)
    return new_credential
def save_credential(credential):
    '''
    Functiona to save credential
    '''
    credential.save_credential
def del_credential(credential):
    '''
    Function to delete credential
    '''
    credential.delete_credential
def find_credential(number):
    '''
    Function to find a credential by number
    '''
    return Credential.find_by_number(number)
def check_existing_credentials(number):
    '''
    Funtion that checks if a acrdential exists with that number and return a boolean
    '''
    return Credential.credential_exist(number)
def display_credentials():
    '''
    Function 
    '''
    return Credential.display_contacts()
##user
def create_user(a_name,u_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(a_name,u_name,password)
    return new_user
def save_newuser(user):
    '''
    function to save new users
    '''
    User.new_user.save_newuser()
def test_deleteuser(user):
    '''
    to test if we can delete a user
    from our user list
    '''
    User.new_user.deleteuser()

def find_userbyappname(user):
    '''
    finding a password using aname
    '''
    return User.find_credentialbyappname(user)

def user_exist(appname):
    '''
    check if user exists
    '''
    return User.user_exist(appname)

def display_alluser():
    '''
    displaying all users
    '''
    return User.display_allusers()
##main function
def main():
    print("Hello Welcome to *PASSWORD_VAULT*. What is your name?")
    user= input()

    print(f"Hello {user}. what would you like to do?.\n To proceed,Use these short codes: \n ca - create an account using your own password \n ra - create an account using a randomly generated  password \n ex - exit the application")
    print('\n')
    short_code = input().lower()
    while True:
            if short_code == 'ca':
                print("Create an account using your own password")
                print("*"*10)

                print("First Name ")
                fname = input()

                print("Last Name ")
                lname = input()

                print("User Name ")
                uname = input()

                print("Phone Number ")
                pnumber = input()
                
                print("Email ")
                email = input()
                
                print("Password ")
                password = input()

                            ##create and save a new credential
                save_credential(create_credential(fname,lname,uname,pnumber,email,password))
                print('\n')
                print(f"New Account {uname} successfully created!")
                print('\n')
                print("To proceed use the short code: \n lg - login into account \n ex - to exit the application")
                short_codetwo = input().lower()
                if short_codetwo == 'lg':
                    print("-"*10)
                    print("LogIn")
                    print("-"*10)
                    print("To log in, input your username and password")

                    print("UserName")
                    user_namein = input()
                        
                    print("Password")
                    pass_wordin = input()
                    ###verifying the username and password
                    if user_namein == uname and pass_wordin == password:
                        print("Access granted.\n To proceed use the following shortcodes: \n ca - create an account using your own password \n ra - create an account using a randomly generated  password \n ex - exit the application")
                        short_codethree = input().lower()
                        if short_codethree == 'cc':
                            print("_"*10)

                            print("username")
                            u_name = input()

                            print("Password")
                            password = input()
                                ###create and save a new user
                            save_newuser(create_user(a_name,u_name,password))
                            print('\n')
                            print("-"*10)
                            print(f"New Credential for {a_name} created.")
                            print('\n')
                            print("-"*10)
                            continue
                        
                        
                        elif short_codethree == 'dc':
                            if display_allusers():
                                print("Here is a list of all your contacts")
                                print('\n')

                                for user in display_allcredentials():
                                    print(f"{user.a_name} {user.u_name} {user.password}")  
                                    print('\n')
                            else:
                                print('\n')
                                print("You do not seem to have any user saved yet.")
                                print('\n')
                        elif short_codethree == 'fc':
                            print("Enter the application name for the credential you want to search for.")

                            search_applicationname =input()
                            if credential_exist(search_applicationname):
                                search_credential = find_credentialbyappname(search_applicationname)
                                print(f"{search_applicationname.a_name} {search_applicationname.u_name} {search_applicationname.password}")                                             
                            else:
                                print("That credential doesnot exist.")
                    else:
                        print("Wrong username or password.Please try again.")
                    
                elif short_codetwo == 'ex':
                    print("Bye Bye!")
                    break
                else:
                    print("I really didn't get that.Please use the short codes")


            elif short_code == 'ra':
                print("Create an account using a randomly generated password")
                print("-"*10)

                print("First Name ")
                fname = input()

                print("Last Name ")
                lname = input()

                print("User Name ")
                uname = input()

                print("Phone Number ")
                pnumber = input()
                
                print("Email ")
                email = input()

                chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                password = "".join(random.choice(chars) for _ in range(8))
                print(f"\nYour password is: **{password}**")

                save_credential(create_credential(fname,lname,uname,pnumber,email,password))
                print('\n')
                print(f"New Account {uname} successfully created!")
                print('\n')
                print("To proceed use the short code: \n lg - login into account \n ex - to exit the application")
                short_codetwo = input().lower()
                if short_codetwo == 'lg':
                    print("-"*10)
                    print("LogIn")
                    print("-"*10)
                    print("To log in, input your username and password")

                    print("UserName")
                    user_namein = input()
                        
                    print("Password")
                    pass_wordin = input()
                    ###verifying the username and password
                    if user_namein == uname and pass_wordin == password:
                        print("*ACCESS GRANTED*.\n To proceed use the following shortcodes: \n cc - create a new credential \n dc - display user \n fc - find a credential by inputing the appname \n rc - to delete a credential \n ex - exit the application")
                        short_codethree = input().lower()
                        if short_codethree == 'cc':
                            print("-"*10)
                            print("To create a new user,Input the following.")
                            print("-"*10)

                            print("Application Name")
                            a_name = input()

                            print("Account Name")
                            u_name = input()

                            print("Password")
                            password = input()
                                ###create and save a new credential
                            save_newcredential(create_credential(a_name,u_name,password))
                            print('\n')
                            print("-"*10)
                            print(f"New Credential for {u_name} created.")
                            print('\n')
                            print("-"*10)
                            continue
                        
                        elif short_codethree == 'dc':
                            if display_allcredentials():
                                print("Here is a list of all your contacts")
                                print('\n')

                                for user in display_allcredentials():
                                    print(f"{user.a_name} {user.u_name} {user.password}")  
                                    print('\n')
                            else:
                                print('\n')
                                print("You do not seem to have any user saved yet.")
                                print('\n')
                        elif short_codethree == 'fc':
                            print("Enter the application name for the credential you want to search for.")

                            search_applicationname =input()
                            if credential_exist(search_applicationname):
                                search_credential = find_credentialbyappname(search_applicationname)
                                print(f"{search_applicationname.a_name} {search_applicationname.u_name} {search_applicationname.password}")                                             
                            else:
                                print("That credential doesnot exist.")
                    else:
                        print("Wrong username or password.Please try again.")
                    
                elif short_codetwo == 'ex':
                    print("Goodbye!")
                    break
                else:
                    print("I really didn't get that.Please use the short codes")
                    break
                
            elif short_code == "ex":
                print("Goodbye!")
                break
            else:
                print("I really didn't get that.Please use the short codes")
                break
if __name__ == '__main__':

    main()