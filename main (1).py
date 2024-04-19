############### Blackjack Project #####################

from art import logo
import random
from replit import clear


def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
  """Compare the user and computer scores and return the result"""
  if user_score == computer_score:
    return "It's a draw."
  elif computer_score == 0:
    return "You lose, opponent has Blackjack."
  elif user_score == 0:
    return "You win with a Blackjack."
  elif user_score > 21:
    return "You went over. You lose."
  elif computer_score > 21:
    return "Opponent went over. You win."
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose."


def play_game():
  """Main function"""
  user_cards = []
  computer_cards = []
  game_over = False

  for i in range(2):
    computer_cards.append(deal_card())
    user_cards.append(deal_card())

  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      if input("\nType 'y' to get another card, type 'n' to pass: ") == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True

  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"\n  Your final hand: {user_cards}, final score: {user_score}")
  print(
      f"  Computer's final hand: {computer_cards}, final score: {computer_score}"
  )
  print(compare(user_score, computer_score))


while input(
    "\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  clear()
  print(logo)
  play_game()
