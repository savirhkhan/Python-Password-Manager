import sys
import shelve
import pyperclip

account = str(input("Enter the UserName: "))
passwordFile = shelve.open(r"C:\password")

def addAccount(na):
    passwordFile[na] = str(input("Enter the Password for " + na + ':'))
    print("*Username and Password is successfully added *")

if not account == '':
    try:
        password = passwordFile[account]
        pyperclip.copy(password)
        print('Password for UserName: ' + account + ' copied to clipboard.')
    except:
        check = input("Sorry! Account is not added in Password Manager, Do You want to add this?(yes/no)")
        if check == 'yes':
            addAccount(account)
        else:
            sys.exit()


