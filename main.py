#Everything works well except that the list of guesses needs to be reset.
#To do that, just add p_guesses = [] at the point the game restarts.

import random


p_num = -100
p_guesses = []
r_guesses = 8
p_games = 0
c_games = 0
g_again = False
play = True

while play:
  ran_num = random.randint(1,100)
  while p_num != ran_num and r_guesses > 0:
    print(f"Your previous guesses were: {p_guesses}")
    p_num = int(input("Guess a number from 1 to 100: "))
    p_guesses.append(p_num) 
    r_guesses = r_guesses - 1
  
    
    if p_num > ran_num:
      print("Too high, guess again!")
      print(f"You have: {r_guesses} guesses left!")
    elif p_num < ran_num:
      print("Too low, guess again!")
      print(f"You have: {r_guesses} guesses left!")
  
  
  if r_guesses == 0:
    c_games = c_games + 1
    print(f"You have won {p_games} while the computer has won {c_games}!")
    print("You lose!")
    p_again = input("Play again? Yes or No? ")
  
    if p_again == "Yes":
      p_num = -100
      r_guesses = 8
      ran_num = random.randint(1,100)
  
    if p_again == "No":
      pass
  
  if p_num == ran_num:
    p_games = p_games + 1
    print("You win!")
    print(f"You have won {p_games} while the computer has won {c_games}!")
    p_again = input("Play again? Yes or No? ")
  
    if p_again == "Yes":
      g_again = True
      p_guesses = []
      r_guesses = 8
  
    elif p_again == "No":
      pass
  
    elif p_again != "Yes" or "No":
      print("Invalid response. Please type Yes or No!")
      p_again = input("Play again? Yes or No? ")