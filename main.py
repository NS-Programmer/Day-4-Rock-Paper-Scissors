import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#ask user for their input 
user_choice = input("What do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors? \n") 
#ask computer for a random input 
print ("You chose: ") 
#convert from input string to integer 
user_choice = int (user_choice)
#prints user choic 
if user_choice == 0: 
  print (rock)
elif user_choice == 1: 
  print (paper)
elif user_choice == 2: 
  print (scissors)

  
computer_choice = random.randint (0,2) 
print ("Computer chose: ")
if computer_choice== 0: 
  print (rock)
elif computer_choice == 1: 
  print (paper)
elif computer_choice == 2: 
  print (scissors)

#Rock (0) vs Scissors (2)
if user_choice > 3: 
  print ("invalid number, try again")
elif user_choice == 0 and computer_choice == 2: 
  print ("You win")
#Scissors (2) vs Paper (1)
elif user_choice == 2 and computer_choice == 1: 
  print ("You win") 
#Scissors (1) vs Paper (0) 
elif user_choice == 1 and computer_choice == 0: 
  print ("You win")
#For when you pick the same as the computer
elif user_choice == computer_choice: 
  print ("It is a draw")
# any other combo and the computer wins 
else: 
  print ("You lose")