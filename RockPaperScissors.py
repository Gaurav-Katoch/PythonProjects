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

game_images = [rock, paper, scissors]

x = 0
while x == 0:
  choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  comp_choice = random.randint(0,2)

  if choice >= 3 or choice < 0:
    print("You typed invalid number, you lose!\n")
  else:
    print("You chose: \n", game_images[choice])
    print("Computer chose: \n", game_images[comp_choice])

    # Game logic and result
    if choice == 0 and comp_choice == 2:
      print("You Win!\n")
    elif choice == 2 and comp_choice == 0:
      print("You Lose!\n")
    elif comp_choice > choice:
      print("You Lose!\n")
    elif comp_choice == choice:
      print("It's Draw!\n")
    elif comp_choice < choice:
      print("You Win!\n")
    else:
      print("You typed invalid number, you lose!\n")

    again = input("Type y to play again : ")
    if again == 'y' or again == 'Y':
      x = 0
    else:
      x += 1