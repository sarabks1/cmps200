import sys

def shift(k, c):
    n = ord(c)
    if(65 <= n <= 90-k or 97 <= n <= 122-k): #if it is lower or upper case and no need to wrap
        return chr(n+k)
    elif 90-k < n <= 90 : #lower case wrap
        return chr(65+90-n)
    elif 122-k < n <= 122: #upper case wrap
        return chr(97+122-n)
    else: #if it is not a char, ( digit, whitespace ect)
        return c

def encrypte(str, k):
    result = ''
    for c in str:
        result += shift(k,c)
    return result

n = int(sys.argv[1])
st = sys.argv[2]
print(encrypte(st, n))
