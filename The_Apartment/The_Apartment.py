#Python Text Game: The Apartment!
import random
random_number = random.randint(0, 3)

# Game Data
clothes = ["A suit and tie", "Dress", "swimwear"]
food = ["apple", "bannana", "hotdog", "green hotdog"]
monsters = []
people = ["Ashley", "Genny", "Tevor" ] 

#Intro
name = input("What is your name?: ")
age = int(input("Your age?: "))
gender = input("Your gender?: ")
 
if age > 0:
    print("Hello", gender, name, "")
else:
    print("You literally arn't even alive!!")

#Chapter 1
print("You awake in your apartment laying in your bed")
print(name + " eats a " + food[random_number])

options = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")