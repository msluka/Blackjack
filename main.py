import random

def play_blackjack():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    user_cards = random.choices(cards, k=2)
    dealer_cards = random.choices(cards, k=2)

    def calculate_scores(cards_list):
        total = sum(cards_list)
        aces = cards_list.count(11)

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

    def new_card():
        return random.choice(cards)

    def display_status():
        print(f"User cards: {user_cards} Sum: {calculate_scores(user_cards)}")
        print(f"Dealer cards: [{dealer_cards[0]}, ?]\n")

    display_status()

    def user_turn():
        while True:
            user_choice = input("Dear User, if you want to Hit, press 'H'. If not, press any other key:\n")
            if user_choice.lower() == "h":
                user_cards.append(new_card())
                user_scores = calculate_scores(user_cards)
                if user_scores > 21:
                    print("User busted!")
                    print(f"User cards: {user_cards} Sum: {user_scores}\n")
                    return False
                elif user_scores == 21:
                    print("User won!")
                    print(f"User cards: {user_cards} Sum: {user_scores}\n")
                    return True
                else:
                    print(f"User cards: {user_cards} Sum: {user_scores}\n")
            else:
                return True

    if not user_turn(): # Returns True or False to the caller - Main game loop
        return True


    def dealer_turn():
        print(f"Dealer's full cards: {dealer_cards} Sum: {calculate_scores(dealer_cards)}\n")
        while calculate_scores(dealer_cards) < 17:
            dealer_cards.append(new_card())
            print(f"Dealer cards: {dealer_cards} Sum: {calculate_scores(dealer_cards)}")

        dealer_score = calculate_scores(dealer_cards)
        user_score = calculate_scores(user_cards)

        if dealer_score > 21 or user_score > dealer_score:
            print("User won!")
        elif user_score < dealer_score <= 21:
            print("Dealer won!")
        else:
            print("It's a draw!")

    dealer_turn()

    should_continue = input("Do you want to continue? (y/n): ").lower()
    return should_continue == "y"
    """
    if should_continue == "y":
        return True
    else:
        return False
    """


# Main game loop
play_again = True
while play_again:
    play_again = play_blackjack()
