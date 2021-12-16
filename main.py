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

# import random
# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# print(names[random.randint(0, len(names) - 1)] + " is going to buy the meal today!")
# import random

# random.r
# # Exercise 3 - Treasure Map 
# # 🚨 Don't change the code below 👇
# row1 = ["1", "2", "3"]
# row2 = ["4", "5", "6"]
# row3 = ["7", "8", "9"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# # Write your code below this row 👇
# map[int(position[1]) - 1][int(position[0]) - 1] = "X"


# # Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# # Write your code below this line 👇
# import random
# user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

# computer_choice = random.randint(0, 2)

# print("Computes Hand")
# if computer_choice == 0:
#   print(rock)
# if(computer_choice ==1):
#   print(paper)
# else:
#   print(scissors)


# winner_result = "You shouldn't see this."
# if user_choice == computer_choice:
#     winner_result = "DRAW"
# elif user_choice == 0:
# if(computer_choice == 2):
#     winner_result = "USER WINS"
#   else:
#     winner_result = "COMPUTE WINS"
# elif user_choice == 1:
#   if(computer_choice == 0):
#     winner_result = "USER WINS"
#   else:
#     winner_result = "COMPUTE WINS"
# else:
#   if(computer_choice == 1):
#     winner_result = "USER WINS"
#   else:
#     winner_result = "COMPUTE WINS"

# print(winner_result)

# SECTION 5: DAY 5 - BEGINNER - PYTHON LOOPS
# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# # Write your code below this row 👇
# sum = 0.0
# count = 0
# for student in student_heights:
#     sum += float(student)
#     count += 1
# average = sum/count
# print(round(average))

# # 5.2
# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# # Write your code below this row 👇
# potato = 0
# for score in student_scores:
#     if potato <= score:
#         potato = score
# print(f"The highest score in the class is: {potato}")

# total = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number

# print(total)

# for number in range(1, 101):
#     output = ""
#     if(number % 3 == 0):
#         output += "Fizz"
#     if(number % 5 == 0):
#         output += "Buzz"
#     if(output == ""):
#         output = number
#     print(output)


# # 5 Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_numbers = int(input("How many numbers would you like?\n"))

# charList = []


# for letter in range(0, nr_letters + 1):
#     charList.append(letters[random.randint(0, len(letters) - 1)])
# for symbol in range(0, nr_symbols + 1):
#     charList.append(symbols[random.randint(0, len(symbols) - 1)])
# for number in range(0, nr_numbers + 1):
#     charList.append(numbers[random.randint(0, len(numbers) - 1)])

# password = ""
# random.shuffle(charList)
# for item in charList:
#     password += item
       
# print("Random Output:  " + password)
  
# DAY 6 ROBOT GAME REEBORG'S WORLD
# MAZE
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while not at_goal():    
#     if front_is_clear() and wall_on_right():
#         move()
#     elif wall_on_right() and wall_in_front():
#         turn_left()
#     elif right_is_clear():
#         turn_right()
#         if front_is_clear():
#             move()
#     elif wall_in_front():
#         turn_right()
#     else:    
#         turn_left()


# DAY 7 HANGMAN GAME
import random
# Step 1 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
splitWord = []
wordbank = []
wrong_guess_Count = 0
correct_guess_Count = 0
max_incorrect_guess_amt = 7
game_end = True


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
print("secret word: " + chosen_word)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for char in range(len(chosen_word)):
    wordbank.append("_")

while game_end:
    wrong_guess_flag = True
    guess = input("Guess a letter! ").lower()
    count = 0
    for char in chosen_word:    
        if guess == char:
            wordbank[count] = char
            wrong_guess_flag = False
        count += 1
    print(wordbank)
    if wrong_guess_flag:
        wrong_guess_Count += 1
    if wrong_guess_Count == 0:
        print(stages[7])
    else:
        print(stages[-wrong_guess_Count])  
    print(f"Your number of wrong guesses {wrong_guess_Count}")
    if wrong_guess_Count == max_incorrect_guess_amt:
        print(stages[-wrong_guess_Count])
        print("YOU LOOSE!")
        game_end = False
    if "_" not in wordbank:
        print("YOU WIN")
        game_end = False

       
