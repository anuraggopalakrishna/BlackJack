#blackjack game using procedural python
import random
import sys

#global variables
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_games_won = 0
computer_games_won = 0

#ascii art for the snazz
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

#methods
def display_score(user_games_won, computer__games_won):
    print(f"Your score: {user_games_won}")
    print(f"Computer's score: {computer_games_won}")

def deal():
  return(random.choice(cards))

def calculate_score(cards):
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def result(user_score, computer_score):
    global computer_games_won
    global user_games_won
    if user_score > 21:
        computer_games_won += 1
        return "BUST! You lose"
    elif computer_score > 21:
        user_games_won += 1
        return "Opponent busts. You win!"
    elif user_score == computer_score:
        return "Draw"
    elif computer_score == 21:
        computer_games_won+= 1
        return "BLACKJACK! Computer wins"
    elif user_score == 21:
        user_games_won+=1
        return "BLACKJACK! You win!"
    elif user_score > computer_score:
        user_games_won+=1
        return "You win!"
    else:
        computer_games_won+=1
        return "Computer wins"

#method with the game logic
def play_game():

  print("Welcome to Blackjack!")
  print(logo)

  user_cards = []
  computer_cards = []
  game_over = False

  for _ in range(2):
    user_cards.append(deal())
    computer_cards.append(deal())


  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")

    if user_score >= 21 or computer_score == 21:
      game_over = True
    else:
      hit = input("Type 'y' to get another card and 'n' to stay with current cards. ")
      if hit == "y" or  hit == "Y":
        user_cards.append(deal())
        user_score = calculate_score(user_cards)
      else:
        game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(result(user_score, computer_score))

#main method to run the game

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
    display_score(user_games_won, computer_games_won)