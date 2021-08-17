import pygame
from button import Button

from cards import Card, Deck, Hand

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Constants for the screen width and height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 370


# Constant for Background colour
POKER_GREEN = (53, 101, 77)

# Frames per second
FPS = 30

# Initialize pygame
pygame.init()


# Function to draw the screen
def draw_screen(screen, color):

    screen.fill(color)
    pygame.display.update()


# Setup the game variables
def game_setup():

    # Create the screen and customize the title and icon
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Blackjack")

    # Create the clock to control the fps
    clock = pygame.time.Clock()

    # Create the different buttons
    hit_button = Button(" Hit+ ", (10, 350), 50, 20)
    stand_button = Button(" Stand ", (70, 350), 50, 20)
    replay_button = Button(" Replay ", (130, 350), 50, 20)

    return screen, clock, hit_button, stand_button, replay_button


# Main game function
def blackjack():

    stand_btn_active = False

    (screen, clock, hit_button, stand_button, replay_button) = game_setup()

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player = Hand()
    dealer = Hand()

    for x in range(2):
        player.add_card(deck)
        dealer.add_card(deck)

    # Variable used to control if the game should run
    running = True

    # Game loop
    while running:

        # Frame rate
        clock.tick(FPS)

        # looks at all game events
        for event in pygame.event.get():

            # checks for user input
            if event.type == KEYDOWN:

                # checks if it was the escape key
                if event.key == K_ESCAPE:

                    # stops the application
                    running = False

            # was the close button hit
            elif event.type == QUIT:

                # stops the application
                running = False

        if player.is_bust():

            # Each loop we draw the screen
            draw_screen(screen, POKER_GREEN)

            # Draw the Cards every loop
            dealer.display(screen, deck, 10, 50)
            player.display(screen, deck, 10, 200)

            # Draw the buttons
            replay_button.draw(screen)

            if replay_button.is_clicked():

                player.clear()
                dealer.clear()

                for x in range(2):
                    player.add_card(deck)
                    dealer.add_card(deck)

        elif hit_button.is_clicked():

            player.add_card(deck)

            if player.is_bust():

                # Each loop we draw the screen
                draw_screen(screen, POKER_GREEN)

                # Draw the Cards every loop
                dealer.display(screen, deck, 10, 50)
                player.display(screen, deck, 10, 200)

                # Draw the buttons
                replay_button.draw(screen)

                if replay_button.is_clicked():

                    player.clear()
                    dealer.clear()

                    for x in range(2):
                        player.add_card(deck)
                        dealer.add_card(deck)

            else:

                # Each loop we draw the screen
                draw_screen(screen, POKER_GREEN)

                # Draw the Cards every loop
                dealer.dealer_display(screen, deck, 10, 50)
                player.display(screen, deck, 10, 200)

                # Draw the buttons
                hit_button.draw(screen)
                stand_button.draw(screen)

        elif stand_button.is_clicked() or stand_btn_active or player.worth == 21:

            stand_btn_active = True

            while dealer.worth < 17:
                dealer.add_card(deck)

            if dealer.is_bust():

                # Each loop we draw the screen
                draw_screen(screen, POKER_GREEN)

                # Draw the Cards every loop
                dealer.display(screen, deck, 10, 50)
                player.display(screen, deck, 10, 200)

                # Draw the buttons
                replay_button.draw(screen)

                if replay_button.is_clicked():

                    player.clear()
                    dealer.clear()

                    for x in range(2):
                        player.add_card(deck)
                        dealer.add_card(deck)

                    stand_btn_active = False

            elif player.worth == dealer.worth:

                # Each loop we draw the screen
                draw_screen(screen, POKER_GREEN)

                # Draw the Cards every loop
                dealer.display(screen, deck, 10, 50)
                player.display(screen, deck, 10, 200)

                # Draw the buttons
                replay_button.draw(screen)

                if replay_button.is_clicked():

                    player.clear()
                    dealer.clear()

                    for x in range(2):
                        player.add_card(deck)
                        dealer.add_card(deck)

                    stand_btn_active = False

            elif player.worth > dealer.worth:

                # Each loop we draw the screen
                draw_screen(screen, POKER_GREEN)

                # Draw the Cards every loop
                dealer.display(screen, deck, 10, 50)
                player.display(screen, deck, 10, 200)

                # Draw the buttons
                replay_button.draw(screen)

                if replay_button.is_clicked():

                    player.clear()
                    dealer.clear()

                    for x in range(2):
                        player.add_card(deck)
                        dealer.add_card(deck)

                    stand_btn_active = False

            elif player.worth < dealer.worth:

                # Each loop we draw the screen
                draw_screen(screen, POKER_GREEN)

                # Draw the Cards every loop
                dealer.display(screen, deck, 10, 50)
                player.display(screen, deck, 10, 200)

                # Draw the buttons
                replay_button.draw(screen)

                if replay_button.is_clicked():

                    player.clear()
                    dealer.clear()

                    for x in range(2):
                        player.add_card(deck)
                        dealer.add_card(deck)

                    stand_btn_active = False

        else:

            # Each loop we draw the screen
            draw_screen(screen, POKER_GREEN)

            # Draw the Cards every loop
            dealer.dealer_display(screen, deck, 10, 50)
            player.display(screen, deck, 10, 200)

            # Draw the buttons
            hit_button.draw(screen)
            stand_button.draw(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    blackjack()
