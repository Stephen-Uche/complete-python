"""You can do for name in friend_ages.

And again, this is a variable that we can name

whatever we want, but I'm calling it name at this point.

And you can print name.

What happens when you do this is,

you're iterating over the dictionary's keys.

So what you would get here is Rolf, Anne, Charlie, and Bob.

The values, 25, 37, 31, 22, will be ignored

and won't be present anywhere in here.

So if we run this, you'll see that you get the keys back.

If you wanted the values, you could iterate

over friend_ages.values.

And then if we run this, now you'll get

25, 37, 31, 22, so just the ages.

Name, age in friend_ages.items.

And what you're gonna get now

is this tuple of names and ages

that you can de-structure into two variables directly here


"""


friends_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for name, age in friends_ages.items():
    print(f"{name} is {age} years old.")




