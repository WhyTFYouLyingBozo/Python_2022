#7.5 excercises
#Question 1
ice_creams = int(input("How many ice creams do you need"))
if ice_creams <= 20:
	print("Coming right up")
elif ice_creams >= 20:
	print("We don't have enough stock")
#Question 2
user_travel = int(input("How far do you intend to travel"))
if user_travel <= 200:
	print("You're all good to go, have a nice trip")
elif user_travel > 200:
	print("Make sure to fill up before you leave.")
#Question 3
user_age = int(input("How old are you?"))
if user_age >= 18:
	print("You are now considered an adult")
elif user_age <=17:
	print("You are still a minor")
#Question 4
user_favmovie = input("What is your favourite movie?")
if user_favmovie == "Lord of the Rings":
	print("You have excellent taste")
elif user_favmovie != "Lord of the Rings":
	print("Lord of the Rings is better")
#Question 5
user_ask = input("Have you hear of darth Plagueis?")
if user_ask == "no":
	print("Darth Plagueis is a fictional character in the Star Wars franchise. A Sith Lord with the ability to prevent death and create life, Plagueis is the mentor of Palpatine (Darth Sidious). ")