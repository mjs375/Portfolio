import random


"""
SOURCE: https://www.youtube.com/watch?v=t8YkjDH86Y4

TODO: should be a class suit

class Suit:
    def __init__(self,name, symbol, color):
        self.name = name
        self.symbol = symbol
        self.color = color
s=Suit("Diamonds", "◆", "Red")

"""

class Card(object):
    """class Card has attributes suit & value.
    METHODS:
    - show(): prints the card suit & value.
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    #
    def show(self):
        print(f"{self.value} of {self.suit}.")


class Suit():
    def __init__(self, name, symbol, color):
        self.name = name
        self.symbol = symbol
        self.color = color



#
#
#
class Deck():
    """
    METHODS:
    - build(): builds 52-card deck in order.
    - show(): prints entire deck of cards.
    - shuffle(): randomly shuffles deck of cards.
    - draw(): pops off last card of deck, returns to whoever drew.
    """
    def __init__(self):
        self.cards = []
        self.build()
    #
    card_values = {1: 'Ace', 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 'Jack', 12: 'Queen', 13: 'King'}
    #
    def build(self): # build 52 cards
        """Builds a deck of 52 playing cards (in new deck order)."""
        for s in ['Spades', 'Hearts', 'Clubs', 'Diamonds']:
            #--Create a Suit instance:
                # pull from Suit class ... TODO
            #--Get each card:
            for v in range(1,14):
                #--Create Card instance of each card
                self.cards.append(Card(s, Deck.card_values.get(v)))
    #
    def show(self):
        """Show the entire deck of cards"""
        #--For every card in deck, call on its show() method
        for c in self.cards:
            c.show()
    #
    def shuffle(self):
        """Shuffles the deck using the Fisher-Yates method."""
        #--Iterate last card backwards:
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    #
    def drawCard(self):
        """Draw (remove) a single card from the deck."""
        #--Remove 'top' card of deck, return to whoever "drew":
        return self.cards.pop()
#
# # # # # # #  ^class Deck^




class Player():
    def __init__(self, name):
        self.name = name
        self.hand = [] # Player starts off with empty hand

    def draw(self, deck):
        """ Player draws a card from 'deck'."""
        self.hand.append(deck.drawCard())
        return self
    #
    def showHand(self):
        for card in self.hand:
            card.show()
    #
    def discard(self): #(TODO: add a suite/value to inputs so you can choose WHICH card to discard, instead of the last card in hand)
        return self.hand.pop()

"""
### Test card:
demo_card = Card("Clubs", 6)
demo_card.show()
### Test a deck:
deck = Deck()
deck.show() # Prints new deck (unshuffled)
deck.shuffle() # Shuffles deck
deck.show()
card = deck.drawCard()
card.show()

lucy = Player('Lucy')
lucy.draw(deck).draw(deck)
lucy.showHand()
"""


deck = Deck()
lucy = Player('Lucy')
fallon = Player('Fallon')
deck.show()
