# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

#BMI 2.0 

# bmi = round(weight / height**2)
# bmis = str(bmi)

# if bmi < 18.5:
#     print("Your BMI is {bmis}, you are underweight.")
# elif bmi > 18.5 and bmi < 25:
#     print(f"Your BMI is {bmis}, you have a normal weight.")
# elif bmi > 25 and bmi < 30:
#     print(f"Your BMI is {bmis}, you are slightly overweight.")
# elif bmi > 30 and bmi < 35:
#     print(f"Your BMI is {bmis}, you are obese.")
# else:
#     print(f"Your BMI is {bmis}, you are clinically obese.")

# Exercise 3 - Leap Year
# year = int(input("Which year do you want to check? "))
# if year % 4 == 0 and year % 400:
#     print("Leap year.")
# elif year % 4 == 0 and year % 100 != 0:
#     print("Not leap year.")
# elif year % 4 == 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")

# Exercise 4 - Pizza Order Practice
# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# total = 0

# if add_pepperoni == "Y" and size == "S":
#     total += 2
# elif add_pepperoni == "Y":
#     total += 3

# if extra_cheese == "Y":
#     total += 1

# if size == "L":
#     total += 25
# elif size == "M":
#     total += 20
# else:
#     total += 15

# print(f"Your final bill is: ${total}.")

# # Exercise 5 - Love Calculator
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# digit1 = name1.lower().count("t")
# digit1 += name1.lower().count("r")
# digit1 += name1.lower().count("u")
# digit1 += name1.lower().count("e")
# digit1 += name2.lower().count("t")
# digit1 += name2.lower().count("r")
# digit1 += name2.lower().count("u")
# digit1 += name2.lower().count("e")

# digit2 = name1.lower().count("l")
# digit2 += name1.lower().count("o")
# digit2 += name1.lower().count("v")
# digit2 += name1.lower().count("e")
# digit2 += name2.lower().count("l")
# digit2 += name2.lower().count("o")
# digit2 += name2.lower().count("v")
# digit2 += name2.lower().count("e")

# total = str(digit1) + str(digit2)


# if int(total) < 10 or int(total) > 90:
#     print(f"Your score is {total}, you go together like coke and mentos.")
# elif int(total) >= 40 and int(total) <= 50:
#     print(f"Your score is {total}, you are alright together.")
# else:
#     print(f"Your score is {total}.")


# import random
# # Remember to use the random module
# # Hint: Remember to import the random module here at the top of the file.
# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# # 🚨 Don't change the code above 👆 It's only for testing your code.

# # Write the rest of your code below this line 👇
# if(random.randint(0, 1) == 1):
#     print("Heads")
# else:
#     print("Tails")

# print("Num: " + str(random.randint(0, 1)))
