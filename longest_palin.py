

def is_palindrome(st): #the function defined in asst4
    x = 0
    y = len(st) - 1
    same = True
    while(same and x <= y):
        if(st[x] != st[y]):
            same = False
        x += 1
        y += -1
    return same


def longest_palin(st):
    longest = ''
    for i in range(len(st)):
        for j in range(len(st)):
            if(is_palindrome(st[i:j+1])): #if the generated string is palindrome
                if len(st[i:j+1]) > len(longest) : #to keep track of the longest encountered 
                    longest = st[i:j+1]
    return longest

print(longest_palin('43xyyx1')) #test

            

