import random
from art import logo
def deal_card():
    cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user,computer):
    if user == computer:
        return ("Its a draw")
    elif computer == 0:
        return ("You Lost the game")
    elif user == 0:
        return ("You won the game")
    elif user > 21:
        return ("You lost the game")
    elif computer>21:
        return ("You won the game")
    elif computer > user:
        return ("You lost the game")
    else:
        return ("You won the game")

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score=-1
    computer_score=-1
    is_game_over = False

    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards : {user_cards} , Your Score : {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score ==0 or computer_score == 0 or user_score > 21:
            is_game_over=True
        else:
            choice = input("Type 'yes' to get another card, type 'no' to pass : ")
            if choice == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score !=0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand : {user_cards}, Final Score: {user_score}")
    print(f"Computer's final hand : {computer_cards} , Final Score: {computer_score}")
    print(compare(user_score,computer_score))



while input("Do you want to play a game of blackjack ? Type 'yes' or 'no' " ) == "yes":
    
    play_game()