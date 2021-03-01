import random
from art import logo

answer = random.randint(1,100)
attempt = 0
game_mode = ""

print(logo)
print("Welcome to the number guessing game.")
print("The number is between 1 and 100.")

while game_mode != "easy" and game_mode != "hard":
  game_mode = input("Please select difficulty of this game. Type 'easy' or 'hard' : ")
  if game_mode == "easy":
    attempt = 10
  elif game_mode == "hard":
    attempt = 5
  else:
    print("Please select valid game mode. 'easy' or 'hard'.")

end_game = False
while attempt > 0 and not end_game:
  print(f"You have {attempt} attempts remaining to make a guess.")
  guess = int(input("Make a guess: "))
  if guess > answer:
    attempt -= 1
    if attempt > 0:
      print("Too high. Guess again.")
  elif guess < answer:
    attempt -= 1
    if attempt > 0:
      print("Too low. Guess again.")
  else:
    print(f"You got it! The answer is {answer}.")
    end_game = True

if not end_game:
  print(f"You ran out of attempts. The answer is {answer}.")
