
def check_pass(password):
    errors = {
        "uppercase_error" : "You need to have at least 1 uppercase character",
        "lowercase_error" : "You need to have at least 1 lowercase character",
        "num_error" : "You need to have at least 1 number",
        "special_char_error" : "You need to have at least 1 special character",
        "long_error" : "Your password is might be difficult to remember. You should make it shorter",
        "short_error" : "Your password is too short. It will be easy to crack it. Again"
    }

    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    numbers="0123456789"
    specialcharacter="*-#"
    a = 0
    b = 0
    c = 0
    d = 0

    
    if len(password) > 8:
        return errors["long_error"]
    elif len(password) < 8:
        return errors["short_error"]
    else:
        for i in password:
            if (i in uppercase):
                a+=1           
            if (i in lowercase):
                b+=1           
            if (i in numbers):
                c+=1           
            if(i in specialcharacter):
                d+=1
        
        if a > 0 and b > 0 and c > 0 and d > 0:
            return "The password is perfect :)"
        else:
            if a == 0:
                return errors["uppercase_error"]
            elif b == 0:
                return errors["lowercase_error"]
            elif c == 0:
                return errors["num_error"]
            else:
                return errors["special_char_error"]
                


password = input('Enter the password in " " ')
print(check_pass(password))
