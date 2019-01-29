#!/usr/bin/env python3.6
from credential import Credential
from user import User

##credential 
def create_credential(fname,lname,uname,phone,email):
    '''
    Function to create new credentials
    '''
    new_credential = Credential(fname,lname,uname,phone,email)
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
def create_user(a_name,u_name,pas):
    '''
    Function to create a new user
    '''
    new_user = User(a_name,u_name,pas)
    return new_user
##main funcio
def main():
    print("Hello Welcome to *PASSWORD_VAULT*. What is your name?")
    person= input()

    print(f"Hello {person}. what would you like to do?")
    print('\n')

if __name__ == '__main__':

    main()