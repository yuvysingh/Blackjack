# Import random to shuffle the deck list
from random import shuffle
from pygame.image import load
from pygame.transform import scale

# Directory for the card images
image_dir = (
    "/Users/yuvysingh/vs code/balckajack/Blackjack/deck_of_cards/"
)

# Define the different suits
suits = "CDHS"

# Define the different ranks
ranks = (
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "J",
    "Q",
    "K",
    "A",
)

# Give each rank a comparable value
values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 1,
}

# Card class to define different card attributes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.ref = self.suit + self.rank
        # Value obtains the value of the card using the values dictionary
        self.value = values[rank]


# Deck class to create a list with all cards with in it
class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        self.card_images = {}
        for suit in suits:
            for rank in ranks:

                # Instansiate a card and append it to the deck
                card = Card(suit, rank)
                self.deck.append(card)
                self.card_images[card.ref] = image_dir + (card.ref) + ".gif"

    def shuffle(self):

        # Shuffles items in the deck list so players can not cheat
        shuffle(self.deck)

    def deal(self):

        if self.is_empty():  # Check if the deck is empty

            # If it is we refill it
            self.refill()
            return self.deck.pop()

        else:

            # Deal returns the first item in the list (deck) such as a dealer would deal out cards
            return self.deck.pop()

    def is_empty(self):

        if not self.deck:  # This checks if the deck is empty

            return True

        else:
            return False

    def refill(self):

        # Refills the variable self.deck
        for suit in suits:
            for rank in ranks:

                # Instansiate a card and append it to the deck
                card = Card(suit, rank)
                self.deck.append(card)


# Hand class is used to store the values of the card the player is holding
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.worth = 0  # The value of the players hand starts with zero value
        self.score = 0

    # add card method to add cards to players hands
    def add_card(self, deck):
        # Deck.deal() adds the card at the top of the deck to the hand
        added_card = deck.deal()
        self.cards.append(added_card)
        self.worth += added_card.value

    def clear(self):

        # Clears the cards in the players inventory
        self.cards.clear()
        self.worth = 0
        

    def is_bust(self):

        if self.worth > 21:
            return True

        return False

    def display(self, screen, deck, x, y):

        for card in self.cards:
            card_img = load(deck.card_images[card.ref]).convert()

            screen.blit(card_img, (x, y))
            x += 50

    def dealer_display(self, screen, deck, x, y):

        card_img = load(deck.card_images[self.cards[0].ref]).convert()

        screen.blit(card_img, (x, y))
