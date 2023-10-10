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


game_images = [rock, paper, scissors]
user_choice = int(input("Type 0 for Rock 1 for Paper or 2 for Scissors\n"))

if user_choice != "rock" or "paper" or "scissors":
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])
    pc_choice = random.randint(0, 2)



    print(f"Computer chose")
    print(game_images[pc_choice])



    if user_choice == 0 and pc_choice == 1:
        print("Pc wins, game over")
    elif user_choice == 0 and pc_choice == 2:
        print("User wins")
    elif user_choice == 1 and pc_choice == 0:
        print ("User wins")
    elif user_choice == 1 and pc_choice == 2:
        print("Pc wins")
    elif user_choice == 2 and pc_choice == 0:
        print("Pc wins")
    elif user_choice == 2 and pc_choice == 1:
        print("User wins")
    elif user_choice == pc_choice:
        print("It's a draw!")
    else:
        print ("game over")    