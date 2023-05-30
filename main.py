from replit import clear
import random
from art import logo


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  current_score = sum(cards)
  if 11 in cards and current_score > 21:
      cards.remove(11)
      cards.append(1)
  if 11 in cards and len(cards) == 2 and current_score == 21:
    return 0
  return current_score

def compare(user_score, computer_score):
    if user_score == computer_score:
      return "It's a draw."
    elif computer_score == 0:
      return "Opponent has Blackjack. You lose."
    elif user_score == 0:
      return "You have a Blackjack. You win."
    elif user_score > 21:
      return "You went over 21. You lose."
    elif computer_score > 21:
      return "Opponent went over. You win."
    elif user_score > computer_score:
      return "You win."
    else:
      return "You lose."


def game():
  print(logo)
  user_cards = []
  computer_cards = []
  game_over = False
  
  for card in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score: {user_score}.")
    print(f" Computer first card: {computer_cards[0]}.")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      if input("Do you want to draw another card? Type 'y' or 'n'.\n") == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True
      
  while computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"Your final cards: {user_cards}, final score: {user_score}.")
  print(f"Computer final cards: {computer_cards}, final score: {computer_score}.")
    
  print(compare(user_score, computer_score))

while input("Do you want to play a Blackjack?\nType 'y' or 'n'\n").lower() == 'y':
  clear()
  game()
