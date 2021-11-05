email = input('write your e-mail: ')

def email_check(email):
    if "@" in email and "." in email:    
        return True
    else: 
        return False

if email_check(email) == True:
    print("valid e_mail")
else:
    print("wrong e_mail")