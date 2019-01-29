import unittest ##import unittest module
from user import User ##import User class from user.py file
class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test case
        '''
        self.new_user = User("twitter","iankabugi","1234pass") #create user object
    def tearDown(self):
        '''
        cleans up after each test case has 
        been executed
        '''
        User.user_list = []
    def test_init(self):
        '''
        to test if object is initialised properly
        '''
        self.assertEqual(self.new_user.app_name,"twitter")
        self.assertEqual(self.new_user.user_name,"iankabugi")
        self.assertEqual(self.new_user.account_password,"1234pass")
if __name__ == '__main__':
    unittest.main()
    def test_save_newuser(self):
        '''
        to test if user object is saved
         into user list
        '''
        self.new_user.save_newuser()
        self.assertEqual(len(users.user_list),1)
    def test_save_multipleuser(self):
        '''
        to test if we can save multiple users
        to the user list
        '''
        self.new_user.save_newuser()
        test_user = users("testapp","testuser","testpass")
        test_user.save_newuser()
        self.assertEqual(len(users.user_list),2)
    def test_deleteuser(self):
        '''
        to test if we can delete a user
        from our user list
        '''
        self.new_user.save_newuser()
        test_user = users("testapp","testuser","testpass")
        test_user.save_newuser()
        self.new_user.deleteuser()
        self.assertEqual(len(users.user_list),1)
    def test_find_userbyappname(self):
        '''
        test to check if we can find a user by using
        the application name and display information
        '''
        self.new_user.save_newuser()
        test_user = users("newapp","testuser","testpass")
        test_user.save_newuser()
        found_user = users.find_userbyappname("newapp")
        self.assertEqual(found_user.account_name,test_user.account_name)
    def test_user_exists(self):
        '''
        test to check if we can get a boolean 
        if a user cannot be found
        '''
        self.new_user.save_newuser()
        test_user = users("newapp","testuser","testpass")
        test_user.save_newuser()
        user_exists = users.user_exist("newapp")
        self.assertTrue(user_exists)
    def test_display_allusers(self):
        '''
        test for method that returns 
        all users saved
        '''
        self.assertEqual(users.display_allusers(),users.user_list)
