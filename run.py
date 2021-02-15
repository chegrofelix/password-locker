#!/usr/bin/env python3.8

import os
from credential import Credential
from user import User
import random

# def create_credentials(first_name, last_name, user_email):
#     '''
#     A function that creates a new users credentials
#     '''

#     new_user_credential = Credential(first_name, last_name, user_email,)
#     return new_user_credential

# def create_user_account(first_name, last_name, user_name, user_email, user_password):
#     '''
#     Function that creates a new user account
#     '''
#     new_user_account = User(first_name, last_name, user_name, user_email, user_password)
#     return new_user_account

# def save_credential(credential):
#     '''
#     A function that saves the new users credentials
#     '''
#     credential.save_credential()

# def save_user_account(user):
#     '''
#     A function that saves the new users account details
#     '''
#     user.save_user_account()

# def delete_credential(credential):
#     '''
#     A function that deletes the new user's credentials
#     '''
#     credential.delete_credential()

# def search_user_email(credential):
#     '''
#     A function that searches for a user's credentials
#     '''
#     credential.search_user_email()

# def credential_exist(credential):
#     '''
#     A function that checks if the credentials of the email being searched for exists
#     '''
#     credential.credential_exist()

# def display_credential(credential):
#     '''
#      display_credential this method that retuns the list of credential_list
#      '''
#     credential.display_credential()

# def display_user_account(user):
#     '''
#     A function that displays the user's account 
#     '''
#     user.display_user_account()

def main():
    print("Hi,Hello!! Welcome PassLock Credentials Check. Enter User First Name.")
    first_name = input()

    print(f"Hey {first_name} you're a step into PassLock. Please enter your last name.")
    last_name = input()

    print(f"Hey {first_name} {last_name} input your credential user email ")
    user_email = input()

    user_in = int(input("Reply with 1 to enter password or 2 to generate a new password for you"))
    if user_in ==1:
        password = input("Enter password: ")
        conf_pass = input("Confirm password: ")
        while password !=conf_pass:
            print("password does not match")
            conf_pass = input("Confirm password: ")
    else:
        pass_len = int(input("Specifiy password length: "))
        password = User.generate_password(pass_len)
        print(f"The generated password is {password}")

    print(f"Congratulations {first_name} {last_name}! Welcome to PassLock!!")
    print('\n')
    account_user = User(first_name,last_name,user_email,password)

    while 1:
        print('*'*70)
        print('*'*70)
        print("For easier navigation through PassLock use the short codes below:\n cc - create an account with a user-define password \n dis - display credentials \n del - delete account \n va - view account \n ex - Exit PassLock ")
        short_code = input()
        short_code = short_code.lower()
        print("short_code",short_code)

        if short_code == "cc":
            
            print("What account would you like to add or create credentials for??ie Twitter, Instagram or Palmchat")
            account_name = input()

            print("Username")
            username = input()

            print("1. Enter password\n2. Generated Password")
            user_in = int(input())
            if user_in ==1:
                password = input("Enter password: ")
            else:
                pass_len = int(input("Password length: "))
                password = account_user.generate_password(pass_len)
                print(f"generated password is '{password}'")
            account_user.save_credential(account_name,username,password)           
            print(f"A {account_name} has successfully been created.")
            print(f"The user account name is {account_name} and the password {password}")
            print('\n')

        elif short_code == "dis":
                if account_user.display_credential() !=[]:
                    print("Here are your User Account Credentials")
                    for account in account_user.display_credential():
                        print(account,'\n')
                
                else:
                    print("Oops!! Credentials not found Please Create an Account using the short code cp")
                    print('\n')

        elif short_code=="del":
            while 1:
                user_in = input("Account name: ")
                if account_user.credential_exist(user_in):
                    account_user.delete_credential(user_in)
                    print("account deleted successfully!")
                    break
                else:
                    print("account does not exist")
        elif short_code == "ex":
            account_user.logout()
            print("PASSLOCK BIDS BYE....THANK YOU FOR VISITING")
            break
        elif short_code == 'va':
            while 1:
                user_in = input("Account name: ")
                if account_user.credential_exist(user_in):
                    print(account_user.view_account(user_in))
                    break
                else:
                    print("Account does not exist")

        else:
            print("Invalid short code please use: \n cc - create an account with a user-define password \n dis - display credentials \n cp - create a PassLock account with an auto-generated password \n va - view account \n ex - Exit PassLock ")

if __name__ == '__main__':
    main()