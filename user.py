import random
from credential import Credential
class User(Credential):
    """
    Class that generates a new instance User
    """


    def __init__(self, first_name, last_name,  user_email, user_password):
        
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.user_password = user_password
        self.isLoggedIn = True
    
    def login(self,email,password):
        if email == self.user_email and password ==self.user_password:
            self.isLoggedIn = True
            return True
        else:
            self.isLoggedIn = False
            return False

    def logout(self):
        self.isLoggedIn = False
        return True