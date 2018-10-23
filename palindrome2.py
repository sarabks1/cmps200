
def is_palindrome(st):
    if len(st) == 0 or len(st) == 1: #True if the length is 1 or 0
        return True
    elif st[0] == st[-1]: #if first and last element are equal
        return is_palindrome(st[1:len(st)-1]) #check if the string excluding first and last chars is palindrome
    else: #if first and last are different, it can not be palindrome
        return False

print(is_palindrome('whyihw'))