from secrets import choice
from string import ascii_letters, digits,punctuation
class Credential:
    '''
    a class that creates a new instance of credential
    '''

    account_list = []

    def generate_password(self,pass_len=8):
        random_str = ascii_letters+punctuation+digits
        password = "".join(choice(random_str) for x in range(pass_len))
        # import pdb; pdb.set_trace()
        return password



    def save_credential(self,name,username,password):

        '''
        save_credential mothod saves the user credentials into the credential_list
        '''
        new_account = dict(name=name,username=username,password=password)
        self.account_list.append(new_account)
        return True

    
    def delete_credential(self,name):

        '''
        delete_credential method allows the user to delete the credentials from the credential_list
        '''
        self.account_list = [x for x in self.account_list if x["name"] !=name]
        return True

    def credential_exist(self, account_name):
        '''
        credential_exist this method checks if the credentials of the email being searched for exists
        
        Arg:
            user_email: the user email to search if exists
        Return:
            Boolean: True or False
        '''

        for credential in self.account_list:
            if credential['name'] == account_name:
                return True
        return False

    
    def display_credential(self):
        '''
        display_credential this method that retuns the list of credential_list
        '''
        return self.account_list

    def view_account(self,name):
        for account in self.account_list:
            if account['name']==name:
                return account