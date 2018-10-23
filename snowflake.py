import turtle

def fractal(order, length):
    l = length / 3
    if order == 0: #base case
        turtle.forward(length)
    elif order == 1: #base case
        turtle.forward(l)
        turtle.left(60)
        turtle.forward(l)
        turtle.right(120)
        turtle.forward(l)
        turtle.left(60)
        turtle.forward(l)
    else: #general case 
        fractal(order-1,l)
        turtle.left(60)
        fractal(order-1,l)
        turtle.right(120)
        fractal(order-1, l)
        turtle.left(60)
        fractal(order-1,l)


def snowflake(order, length):
    for i in range(3): #since the snowflake is an equilateral triangle
        fractal(order, length)
        turtle.right(120)

snowflake(3, 300)
turtle.done()
