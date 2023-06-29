#Game of blackjack where the ace is 11 and its going to count as 11 until the user goes over 21. We also assume we have
#an infinite depth so it means that when a card is drawn from the deck it is not removed from the deck where as in a
#casino they have maybe 6 or 8 decks of cards and when a card is drawn there is less probability of that card being drawn again.
#However we want to keep things simple so we assume an infinite deck. REMMEBER THE DEALER KEEPS DRAWING CARDS UNTIL 17 OR
#ABOVE IS REACHED.


#importing random module
import random



blackjack_logo = '''

                                                               
#####  #        ##    ####  #    #      #   ##    ####  #    # 
#    # #       #  #  #    # #   #       #  #  #  #    # #   #  
#####  #      #    # #      ####        # #    # #      ####   
#    # #      ###### #      #  #        # ###### #      #  #   
#    # #      #    # #    # #   #  #    # #    # #    # #   #  
#####  ###### #    #  ####  #    #  ####  #    #  ####  #    # 

                 '''
goodbye_logo = '''

 _____                 _ _                  _ 
|  __ \               | | |                | |
| |  \/ ___   ___   __| | |__  _   _  ___  | |
| | __ / _ \ / _ \ / _` | '_ \| | | |/ _ \ | |
| |_\ \ (_) | (_) | (_| | |_) | |_| |  __/ |_|
 \____/\___/ \___/ \__,_|_.__/ \__, |\___| (_)
                                __/ |         
                               |___/    
                               
                 '''

#Defining functions


#Draw card function which is used for the intial of drawing of cards. The first round of drawing of cards.
def draw_card_initial():
    #Defining empty lists for list_of_user_cards and list_of_dealers_cards
    list_of_user_cards = []
    list_of_dealer_cards = []

    #setting i = 0
    i = 0

    #While loop that runs as long i < 2
    while i < 2:
        #Randomly selecting users card from cards list
        user_card = random.choice(cards)
        #Appending randomly selected users card to list_of_user_cards
        list_of_user_cards.append(user_card)

        #Randomly selecting dealer_card from cards list
        dealer_card = random.choice(cards)

        #Appending randomly selected users card to list_of_user_cards
        list_of_dealer_cards.append(dealer_card)

        #Selecting first item from list_of_dealer_cards
        revealed_dealer_card = list_of_dealer_cards[0]

        #Increasing value of i by 1
        i += 1

        #User current score
        user_current_score = sum(list_of_user_cards)

        #Dealer current score
        dealer_current_score = sum(list_of_dealer_cards)


    #Printing list_of_user_cards
    print("Your cards are ", list_of_user_cards, "your current score is ", user_current_score)

    #Printing one of the dealers cards.
    print("Dealers first card is ", revealed_dealer_card)

    #Asking user if they would like to draw another card
    another_card = input("Would you like to draw another card? yes/no ")

    #While loop that runs only while another_card equals yes
    while another_card == "yes":

        # Randomly selecting users card from cards list
        user_card = random.choice(cards)
        # Appending randomly selected users card to list_of_user_cards
        list_of_user_cards.append(user_card)

        # # Randomly selecting dealer_card from cards list
        # dealer_card = random.choice(cards)
        #
        # # Appending randomly selected users card to list_of_user_cards
        # list_of_dealer_cards.append(dealer_card)

        # User current score
        user_current_score = sum(list_of_user_cards)
        print("your current score is" , user_current_score)

        # Dealer current score
        dealer_current_score = sum(list_of_dealer_cards)


        #If users cards add up to more than 21 then they are bust if not they are asked if they would like draw another card
        if user_current_score > 21:
            break
        else:
            another_card = input("Would you like to draw another card? yes/no ")


########################################


    # While loop that runs whilst dealers score is less than 17 and user isn't already bust
    while dealer_current_score < 17 and dealer_current_score <= 21:
        # Randomly selecting dealer_card from cards list
        dealer_card = random.choice(cards)
        print("dealer has drawn", dealer_card)

        # Appending randomly selected users card to list_of_user_cards
        list_of_dealer_cards.append(dealer_card)

        # Dealer current score
        dealer_current_score = sum(list_of_dealer_cards)


        # What to do if dealer is bust
        if dealer_current_score > 21:
            break
        # if dealer_current_score is increased to seventeen or above but below 21 by drawing a card.
        if dealer_current_score <= 21 and dealer_current_score > user_current_score:
            break


    print("dealer score is" , dealer_current_score)
    print("user score is" , user_current_score)
    print("dealers cards were", list_of_dealer_cards)
    print("users cards were", list_of_user_cards)


#outcome of the game depending on the scores of the user and the dealer
    if user_current_score > 21 and dealer_current_score <= 21:
        print("user bust, dealer wins!")
    if dealer_current_score > 21 and user_current_score <= 21:
        print("dealer bust, user wins!")
    if dealer_current_score <= 21 and user_current_score <= 21:
        if dealer_current_score < user_current_score:
            print("user wins!")
        if dealer_current_score > user_current_score:
            print("dealer wins!")
        if dealer_current_score == user_current_score:
            print("draw!")






    return





#List of available cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#Asking user if they want to play a game of blackjack
play = input("Do you want to play a game of blackjack? yes/no ")

#What to do if user does/doesn't want to play
if play == "yes":
    print(blackjack_logo)

    #Calling draw_card function
    draw_card_initial()

if play == "no":
    print(logo)






