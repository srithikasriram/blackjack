import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10]
def checkBlackJack(card_list_one, card_list_two):
    """checks if users cards or comp's cards add to 21, returns true if either does and false if they do not"""
    sum_one = 0
    for card in card_list_one:
        sum_one += card
    sum_two = 0
    for card in card_list_two:
        sum_two += card
    if sum_one == 21 and sum_two == 21:
        print("Both win! Both have blackjack!")
        return True
    elif sum_one == 21:
        print("User wins! User has blackjack")
        return True
    elif sum_two == 21:
        print("Computer wins! User has blackjack")
        return True
    return False

def display_scores(user_list, user_score, comp_list):
    """displays user's cards, user's score, and computer's first card"""
    print(f"Your cards are {user_list}, current score is {user_score}. \n Computer's first card: {comp_list[0]}")

def calculate_score(list):
    """calculates the sum of the cards in the list"""
    sum = 0
    for card in list:
        sum += card
    return sum

rerun = True
while rerun:
    choice = input("Do you want to play blackjack? 'y' or 'n': ")
    if choice == "y":
        user_cards = []
        comp_cards = []

        # create deck
        for i in range(2):
            user_cards.append(random.choice(cards))
            comp_cards.append(random.choice(cards))

        # calculate initial scores and display to user
        user_sum = calculate_score(user_cards)
        comp_sum = calculate_score(comp_cards)
        display_scores(user_cards, user_sum, comp_cards)

        # determines if user needs to add more cards
        user_choice_to_draw = True
        if checkBlackJack(user_cards, comp_cards):
            user_choice_to_draw = False
        
        while user_choice_to_draw:
            user_choice_to_draw_input = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice_to_draw_input == 'y':
                user_cards.append(random.choice(cards))
                user_sum = calculate_score(user_cards)
                display_scores(user_cards, user_sum, comp_cards)
                if user_sum == 21:
                    print("User wins")
                if user_sum > 21:
                    if 11 in user_cards:
                        user_cards[user_cards.index(11)] = 1
                        if calculate_score(user_cards) > 21:
                            print("You lose.")
                        else:
                            user_choice_to_draw = True
                    else:
                        print("You lose. ")
            
            while comp_sum < 16:
                new_card = random.choice(cards)
                comp_cards.append(new_card)
                comp_sum += new_card

            print(f"Your final hand: {user_cards}, final score {user_sum}.")
            print(f"Computer's final hand: {comp_cards}, final score: {comp_sum}")
            if user_sum > 21:
                print("You went over. You lose. ")
            elif comp_sum > 21:
                print("The computer went over. You win! ")
            elif user_sum > comp_sum:
                print("You win!")
            elif comp_sum > user_sum:
                print("You lose. ")
            else:
                print("It's a draw.")
            user_choice_to_draw = False
    else:
        print("Game over.")
        rerun = False
