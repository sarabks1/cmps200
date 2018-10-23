
def flatten(lst):
    if lst == []: #base case, empty list
        return []
    elif isinstance(lst[0], list): #if the first item in the list is a list
        return flatten(lst[0] + flatten(lst[1:])) #add the two list to have a list(from 2 lists) than a sublist in a list
    else: #if the first item is an integer, add it to the list and expand the rest of the list
        return [lst[0]] + flatten(lst[1:])


print(flatten([2,9,[2,1,13,2],8,[2,6]]))
