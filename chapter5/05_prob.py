#create empty dict allow 4 friend to enter their favourite language as value and key as their name Assume that nak=mes are Unique


d = {}

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
d.update({name: language})
name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
d.update({name: language})
name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
d.update({name: language})
name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
d.update({name: language})

print(f'Favourite programming languages of friends: {d}')