import sys
# inorder to check if it is a good password we check for each condition if it is satisfied
def long_enough(password): #if it is more than or  8 chars
    return (len(password) >= 8)

def contain_digit(password): #if it contains a digit
    return any(c.isdigit() for c in password)

def contain_upper(password): #if it contains an upper case
    return any(c.isupper for c in password)

def contain_lower(password): #if it contains a lower case
    return any(c.islower() for c in password)

def contain_non_alpha(password): #if it contains a non alphanumeric char
    return any( (not c.isalpha() and not c.isdigit()) for c in password) 
#not c.isalpha may return true if the char is a digit, that's why we have to exclude this case

p = sys.argv[1]

strong_pwd = long_enough(p) and contain_digit(p) and contain_lower(p) and contain_lower(p) and contain_non_alpha(p)
print(strong_pwd)