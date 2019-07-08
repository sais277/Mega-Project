'''

URL:-https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/

Problem:-
create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:

your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later.

Python Solution:-
'''

name=input("Enter name:")
age=int(input("Enter age:"))
uname=input("Enter username:")

print(f'your name is {name}, you are {age} years old, and your username is {uname}')

file=open("/home/sai/PycharmProjects/Reddit-Challenge/user.txt",'a')

file.write(f'your name is {name}, you are {age} years old, and your username is {uname}\n')
