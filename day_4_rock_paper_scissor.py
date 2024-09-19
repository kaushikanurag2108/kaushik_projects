import random

user_choice = ''
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

while user_choice not in ('rock', 'paper', 'scissor'):
    user_choice = input("Choose your luck: Rock, Paper or scissors\n").lower()
    if user_choice not in ('rock', 'paper', 'scissor'):
        print('Invalid choice. Please enter again!')

available_choices = ['rock', 'paper', 'scissor']
computer_choice = random.choice(available_choices)

user_com_list = [user_choice, computer_choice]
user_win_1 = ['rock','scissor']
user_win_2 = ['paper', 'rock']
user_win_3 = ['scissor', 'paper']

if user_choice == 'rock':
    print(f"\nuser choice: {rock}")
elif user_choice == 'paper':
    print(f"user choice: {paper}")
else:
    print(f"user choice: {scissors}")

if computer_choice == 'rock':
    print(f"\nuser choice: {rock}")
elif computer_choice == 'paper':
    print(f"user choice: {paper}")
else:
    print(f"user choice: {scissors}")

if user_choice == computer_choice:
    print("It's a Draw. Play again")
elif user_com_list in (user_win_1, user_win_2, user_win_3):
    print("You won")
else:
    print("You lost. Better luck next time")