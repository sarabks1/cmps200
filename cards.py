import random

# constructs and returns a list of 52 strings representing a deck of cards
def deck():
    list1 = ['Hearts','Diamonds','Spades','Clubs']
    list2 = ['2','3','4','5','6','7','8','9','10','Jack','Queens','King','Ace']
    cards =[]
    for t in list1:
        for s in list2:
            cards.append(t+' of '+s)
    return cards

# returns a list of n cards from a full 52-card deck chosen with replacement
def choose_cards(n):
    chosen = []
    cards = deck()
    for i in range(n):
        t = random.randint(0,51)
        chosen.append(cards[t])
    return chosen

# returns a list of n cards from a full deck without replacement
def draw_cards(n):
    chosen = []
    cards = deck()
    for i in range(n):
        t = random.randint(0,51)
        if(cards[t] in chosen): #if the element has already been selected
            i -= 1 #decremente i to generate another value for this index
        else:
            chosen.append(cards[t]) #if it has not been selected, then it should be appended to the list
    return chosen

# takes in a list of cards and returns a list of four numbers containing how many cards there are in every suit
def suit_count(hand):
    count = [0,0,0,0]
    hearts = 'Hearts'
    diamonds = 'Diamonds'
    spades = 'Spades'
    clubs = 'Clubs'
    for t in hand:
        if (hearts in t):
            count[0] += 1
        elif(diamonds in t):
            count[1] += 1
        elif(spades in t):
            count[2] += 1
        else:
            count[3] += 1
    return count

list1 = ['Hearts','Diamonds','Spades','Clubs']

print('Constructing the deck of cards...')
cards = deck()

print('Selecting a list of 8 cards from the deck with replacement...')
chosen = choose_cards(8)
print(chosen)
print('Suit count: ')
suit = suit_count(chosen)
for i in range(4):
    print(suit[i],' ', list1[i])
print()

print('Selecting a list of 8 cards from the deck without replacement...')
draw = draw_cards(8)
print(draw)
print('Suit count: ')
suit = suit_count(draw)
for i in range(4):
    print(suit[i],' ',list1[i])
