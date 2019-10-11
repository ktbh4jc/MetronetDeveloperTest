import random

# to run: $ python3 CustomSorting.py

def sort_cards(cards, reversed = False):
    values_dictionary = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    suits_dictionary = {'Hearts': 1, 'Diamonds': 2, 'Clubs': 3, 'Spades': 4}
    output = sorted(cards, key=lambda card: suits_dictionary[card.suit], reverse = reversed)
    output.sort(key=lambda card: values_dictionary[card.value], reverse = reversed)
    return output


###################### Below this line was simply to allow me to test locally##################
class Card:
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    def __init__(self):
        self.value = random.choice(self.values)
        self.suit = random.choice(self.suits)
    
    def __str__(self):
      return f'{self.value} of {self.suit}'

def main():
  cards = []
  for _ in range(0, 20):
    card = Card()
    cards.append(card)
  print('\n'.join(map(str, cards)))
  print("\n\nNow sorted")
  print('\n'.join(map(str, sort_cards(cards))))
  print("\n\nAnd reverse sorted")
  print('\n'.join(map(str, sort_cards(cards, True))))
  print('\n\nAnd once more unsorted')
  print('\n'.join(map(str, cards)))



if __name__ == "__main__":
  main()