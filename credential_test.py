import unittest #Importing unittest module
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test Class that defines test cases for the credentials class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        set up method to run before each test
        '''
        self.new_Credential = Credential()

    def save_credential(self):
        '''
        save_credential method that saves credentials into the account_list
        '''
        Credential.account_list.append(self)

if __name__ == '__main__':
    unittest.main()   