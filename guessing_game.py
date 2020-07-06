"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def generate_random(limit):
  random_number = random.randint(1,limit)
  return random_number
  
def request_number():
  is_invalid = True
  
  while is_invalid:
    number_guess = input("Please pick a number between 1 and 10...  ")
    
    try:
      number_guess = int(number_guess)
    except ValueError:
      print("Entry must be a number between 1 and 10")
    else:
      if number_guess > 0 and number_guess <= 10:
        is_valid = False
        return int(number_guess)
      else:
        print("Enty must be a number between 1 and 10");
  
def game_over():
  print("*" * 20)
  print("The game is over!")
  print("*" * 20)
  
def start_game():
    # Header
    high_score = 0
    guess_count = 0
    game_active = True
    game_continue = True
    is_invalid = True
    print("-"*20)
    print("Guess that number")
    print("-"*20)
    
    
    while game_continue:
      current_random = generate_random(10);
      print("Your current high score is {}!".format(high_score))
      while game_active:
        current_guess = request_number()

        if current_guess == current_random:
          guess_count += 1
          print("You guessed it the number is {}! It took {} tries!".format(current_random, guess_count))
          game_active = False
        elif current_guess < current_random:
          guess_count += 1
          print("Your guess of {} was too low!".format(current_guess))
        else:
          guess_count += 1
          print("Your guess of {} was too high!".format(current_guess))
          
      will_continue = input("Would you like to continue?  (Y/N)  ")
      will_continue = will_continue.upper()
      if will_continue == "Y":
        if high_score > guess_count and high_score != 0:
          high_score = guess_count
        elif high_score == 0:
          high_score = guess_count
        guess_count = 0
          
        game_active = True
      else:
        game_continue = False
        game_over()
    
    """
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()