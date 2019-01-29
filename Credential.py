class Credential:
    """
    Class that generates new instances of credentials.
    """

    credential_list = [] # Empty credential list
        # Init method up here
    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

        credential.credential_list.append(self)

    def __init__(self,first_name,last_name,username,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = number
        self.email = email
#code to delete credential      
    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        credential.credential_list.remove(self) 
    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a credential that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            credential of person that matches the number.
        '''

        for credential in cls.credential_list:
            if credential.phone_number == number:
                return credential 
    @classmethod
    def credential_exist(cls,number):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.phone_number == number:
                    return True

        return False
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list  
   