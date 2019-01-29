import string
import secrets
import random
class User:
    '''
    Class that generates new instance of a user
    creates a password
    '''
    user_list = []
    def __init__(self,app_name,user_name,account_password):
        '''
        initialises a new instance of a user
        '''
        self.app_name = app_name
        self.user_name = user_name
        self.account_password= account_password
    def save_newuser(self):
        User.user_list.append(self)
    def deleteuser(self):
        '''
        delete a user from user list
        '''
        User.user_list.remove(self)
    @classmethod
    def find_userbyappname(cls,name):
            '''Method that takes in appname and returns a user
            that matches that appname.
            Args:
            appname to search for
            Returns :
            users of person that matches that appname.
            '''
            for User in cls.user_list:
                if User.app_name == name:
                    return User
    @classmethod
    def user_exist(cls,appname):
        '''
        method that checks if  a user
         exists that uses appname and returns a boolean
        '''
        for users in cls.user_list:
            if users.app_name == appname:
                return True
        return False
    @classmethod
    def display_allusers(cls):
        '''
        method that returns the users list
        '''
        return cls.user_list
    @classmethod
    def copy_account_password(cls,appname):
        user_found = users.find_userbyappname(appname)
        pyperclip.copy(user_found.account_password)