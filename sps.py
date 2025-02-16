import random
n=input("PLEASE ENTER YOUR NAME HERE:- ")
print("WAKAR HUSSAIN WELCOMES YOU TO ROCK PAPER AND SCISSOR (^_-) ")

rock = '''rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissor]
select = int(input("choose 0 for Rock, 1 for paper, 2 for scissor: "))
reply = int(random.random()*3)
# print(game[reply])

if(select==2):
    if(reply==0):
        print("your move:")
        print(game[select])
        print("Computer's move")
        print(game[reply])
        print(f"sad :( {n} You Lose!")
    elif(reply==1):
        print("your move:")
        print(game[select])
        print("Computer's move")
        print(game[reply])
        print(f"Hurray! :) {n} You Win!")
    else:
        print("your move:")
        print(game[select])
        print("Computer's move")
        print(game[reply])
        print("No one wins play again!")

elif(select==1):
    if(reply==0):
        print("your move:")
        print(game[select])
        print("Computer's move")
        print(game[reply])
        print(f"Hurray! :) {n} You Win!")
    elif(reply==1):
        print("your move:")
        print(game[select])
        print("Computer's move")
        print(game[reply])
        print("No one wins play again!")
    else:
        print("your move:")
        print(game[select])
        print("Computer's move")
        print(game[reply])
        print(f"sad :( {n} You Lose!")

elif(select<2):
    print("You have done a wrong move")

else:
    if(reply==0):
        print("your move:")
        print(game[select])
        print("Computer's move")
        print(game[reply])
        print("No one wins play again!")
    elif(reply==1):
        print("your move:")
        print(game[select])
        print("Computer's move")
        print(game[reply])
        print(f"sad :( {n} You Lose!")
    else:
        print("your move:")
        print(game[select])
        print("Computer's move")
        print(game[reply])
        print(f"Hurray! :) {n} You Win!")






