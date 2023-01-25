import random as r
from replit import clear
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = r.choice(cards)
    return random_card


def compare():
    us = user_score
    cs = computer_score
    if us == cs:
        print("draw")
    elif cs == 0 or us > 21:
        print("You lose!")
    elif us == 0 or cs > 21:
        print("You win!")
    elif cs > us:
        print("Computer wins!")
    elif us > cs:
        print("You win!")
        

end = False       
while not end: 
    print(logo)
    choose = int(input("choose amount to bet [$1, $10, $20, $50, $100]: $"))
    print(choose)
    
    def calculate_score(cards):
        """Take a list of cards and return the scores"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if (11 in cards) and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
           
    user_cards = []
    computer_cards = []
    
    game_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f" user: {user_cards}. user_Score = {user_score}")
        print(f"computer: {computer_cards[0]}")
        
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            ask = input("Do you want to draw another card? y/n : ").lower()
            print(ask)
            if ask == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
       
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f" user: {user_cards}. user_Score = {user_score}")
    print(f"computer: {computer_cards}. computer_score = {computer_score}")
    compare()    
    
    restart = input("Do you want to restart the game? y/n: ").lower()
    print(restart)
    if restart == "n":
        print("Game over!")
        end = True
    elif restart == "y":
        clear()
