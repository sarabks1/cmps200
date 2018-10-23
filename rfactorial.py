# recursive version of the function factorial defined earlier
def rfactorial(n):
    if n == 1:
        return 1
    else:
        return n*rfactorial(n-1)

print(rfactorial(4))