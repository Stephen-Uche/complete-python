
"""Destructuring. 
It makes our programmes much more easy to read.

Imagine you've got a tuple of currencies.

Remember, this is how we can create a tuple.

You can put the brackets in here or not

if you don't want to.

You can, just like you do currencies equal 0.8 comma 1.2

you can do USD, EUR equal currencies.

And what this means is we're going to get

the first value of the tuple

and put it into a new variable called USD.

And we're gonna take the second value of the tuple

and we're gonna put into a new variable called EUR.

So you can imagine that 0.8

is the United States dollar conversion rate

and 1.2 is the Euro conversion rate

from pounds of course.

So this is called destructuring.

currencies = 0.8, 1.2
usd, eur = currencies
"""

friends = [
    ("Rolf", 25),
    ("Anne", 37),
    ("Charlie", 31),
    ("Bob", 22)
]

for name, age in friends:
    print(f"{name} is {age} years old")