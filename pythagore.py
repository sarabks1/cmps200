import sys

# checks if a triplet (a,b,c) satisfy the relationship a**2 + b**2 = c**2
def is_pythagorean(tuple):
    a = tuple[0]
    b = tuple[1]
    c = tuple[2]
    if(a**2 + b**2 == c**2):
        return True
    else:
        return False

# checks if the triplet(a,b,c) is not a multiple of (3,4,5)
def is_multiple(tuple):
    a = tuple[0]
    b = tuple[1]
    c = tuple[2]
    if((a/3) == (b/4) == (c/5) != 1):
        return True
    else:
        return False
 
def generate_pytha(n):
    list = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if(i+j+k < n):
                    if(is_pythagorean((i,j,k)) and not is_multiple((3,4,5))): #if it is not a multiple and not the smallest (where quotient =1)
                        list.append((i,j,k))
    return list


n = int(sys.argv[1])
list = generate_pytha(n)
for e in list:
    print(e)


