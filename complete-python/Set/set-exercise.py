"""We have provided you with two variables:

nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set() # This is an empty set, like {}
In this exercise, ask the user for the name of a friend. Add this name to the user_friends set provided.

Finally, print out a set that contains only the name of the friend if the friend is in the nearby_people set.

You'll want to calculate the intersection between two sets, and print the result out.
"""
nearby_people = {"Rolf", "Jen", "Anna"}

user_friends = set()

friend = input("Enter your friends name to see if he is nearby: ")

user_friends.add(friend)

#print(nearby_people)


print(user_friends.intersection(nearby_people))