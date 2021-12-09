import random
import time
def main():
    print("\nWelcome to my casino \nWould you like to play sloat(S) blackjack(B) or roulette(R)")
    game_select=input().lower()
    if game_select == "s":
        slots_hub()
    if game_select == "b":
        blackjack_hub()
    if game_select == "r":
        roulette_hub()
    else:
        print("that's not a game option")
        time.sleep(1)
        exit()
def slots_hub():
    print("welcome to the casino slots machines (it's £1 per go)")
    print("how much would you like to spend?")
    slots_bet=float(input('£'))
    print("ok we will put that on your tab")
    time.sleep(1)
    while slots_bet > 0:
        slots(slots_bet)
def slots(slots_bet):
    slots_numbers=("7","7","7","420","420","420","69","69","69","911","911","911","666","666","666")
    slots1=random.choice(slots_numbers)
    slots2=random.choice(slots_numbers)
    slots3=random.choice(slots_numbers)
    print(slots1,slots2,slots3)
    if (slots1) == "7":
        if slots2 == "7":
            if slots3 == "7":
                print("")
                print("tripple 7's here's £50")
                slots_bet = slots_bet + 50
    if (slots1) == "420":
        if slots2 == "420":
            if slots3 == "420":
                print("")
                print("tripple 420's here's £10")
                slots_bet = slots_bet + 10
    if (slots1) == "69":
        if slots2 == "69":
            if slots3 == "69":
                print("")
                print("tripple 69's here's £10")
                slots_bet = slots_bet + 10
    if (slots1) == "911":
        if slots2 == "911":
            if slots3 == "911":
                print("")
                print("tripple 666's here's £10")
                slots_bet = slots_bet + 10
    if (slots1) == "666":
        if slots2 == "666":
            if slots3 == "666":
                print("")
                print("tripple 911's here's £10")
                slots_bet = slots_bet + 10
    slots_bet=slots_bet-1
    print("your current balance is £",slots_bet)
    print("Press Enter to reroll or type (E) to leave slots")
    slots_end=input().lower()
    print("")
    if slots_end == "e":
        print("---------------------------------------------------------------------------")
        print("your final tab was £", slots_bet)
        main()
    if slots_bet <= 1:
        print("---------------------------------------------------------------------------")
        print("\nyou are out of money sorry")
        main()
    slots(slots_bet)

def blackjack_hub():
    blackjack_total_money=0
    print("--------------------------------------------------------------------------- \nwelcome to blackjack \n\nif you get a higher number than the dealer you win but if you get over 21 you lose \n\n1-10 = their coordinating number \nking, queen, jack = 10 \nace = 11 \nhit pulls another card into your hand \nstand keeps the cards you have in your hand \nforfeit ends the round(you lose your bet though)")
    blackjack(blackjack_total_money)
def blackjack(blackjack_total_money):
    total_card_value=0
    total_dealer_card_value=0
    order=(1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'king','king','king','king','queen','queen','queen','queen','jack','jack','jack','jack','ace','ace','ace','ace')
    print("--------------------------------------------------------------------------- \nwhat is your bet")
    blackjack_bet=float(input("£"))
    input("press enter to get your cards")
    card1=random.choice(order)
    card1_value=card1
    if card1 == "king":
        card1_value=10
    if card1 == "queen":
        card1_value=10
    if card1 == "jack":
        card1_value=10
    if card1 == "ace":
        card1_value=11
    card2=random.choice(order)
    card2_value=card2
    if card2 == "king":
        card2_value=10
    if card2 == "queen":
        card2_value=10
    if card2 == "jack":
        card2_value=10
    if card2 == "ace":
        card2_value=11
    card3=random.choice(order)
    card3_value=card3
    if card3 == "king":
        card3_value=10
    if card3 == "queen":
        card3_value=10
    if card3 == "jack":
        card3_value=10
    if card3 == "ace":
        card3_value=11
    total_card_value=(card1_value+card2_value+card3_value)

    dealer_card1=random.choice(order)
    dealer_card1_value=dealer_card1
    if dealer_card1 == "king":
        dealer_card1_value=10
    if dealer_card1 == "queen":
        dealer_card1_value=10
    if dealer_card1 == "jack":
        dealer_card1_value=10
    if dealer_card1 == "ace":
        dealer_card1_value=11
    dealer_card2=random.choice(order)
    dealer_card2_value=dealer_card2
    if dealer_card2 == "king":
        dealer_card2_value=10
    if dealer_card2 == "queen":
        dealer_card2_value=10
    if dealer_card2 == "jack":
        dealer_card2_value=10
    if dealer_card2 == "ace":
        dealer_card2_value=11
    dealer_card3=random.choice(order)
    dealer_card3_value=dealer_card3
    if dealer_card3 == "king":
        dealer_card3_value=10
    if dealer_card3 == "queen":
        dealer_card3_value=10
    if dealer_card3 == "jack":
        dealer_card3_value=10
    if dealer_card3 == "ace":
        dealer_card3_value=11
    total_dealer_card_value=(dealer_card1_value+dealer_card2_value+dealer_card3_value)
    print("\nyour cards are",card1,card2,card3,"\nyour total card value is",total_card_value) 
    print("\n\nthe dealers cards are",dealer_card1,"?","?")
    print("would you like to Hit(H), stand(S) or forfeit(F)")
    hit_stand_forfeit=input().lower()
    if hit_stand_forfeit == "h":
        card4=random.choice(order)
        card4_value=card4
        if card4 == "king":
            card4_value=10
        if card4 == "queen":
            card4_value=10
        if card4 == "jack":
            card4_value=10
        if card4 == "ace":
            card4_value=11
        total_card_value=(total_card_value+card4_value)
        print("--------------------------------------------------------------------------- \nyour cards are now",card1,card2,card3,card4,"\nyour total is now",total_card_value)
        if total_card_value > 21:
            print("--------------------------------------------------------------------------- \nyour total went over 21, you lose £100")
            blackjack_bet=-100
        elif total_card_value > total_dealer_card_value:
            print("--------------------------------------------------------------------------- \nthe dealers cards are",dealer_card1,dealer_card2,dealer_card3,"\nthe dealers total is",total_dealer_card_value,"\nyou got a higher score than the derler, you win")
            blackjack_bet=blackjack_bet*2
        elif total_dealer_card_value >21:
            print("--------------------------------------------------------------------------- \nthe dealers cards are",dealer_card1,dealer_card2,dealer_card3,"\nthe dealers total is",total_dealer_card_value,"\nthe dealer went over 21, uou win")
            blackjack_bet=blackjack_bet*2
        elif total_dealer_card_value > total_card_value:
            print("--------------------------------------------------------------------------- \nthe dealers cards are",dealer_card1,dealer_card2,dealer_card3,"\nthe dealers total is",total_dealer_card_value,"\nthe dealer got a higher score than you, you lose £100")
        elif total_card_value == total_dealer_card_value:
             print("--------------------------------------------------------------------------- \nthe dealers cards are",dealer_card1,dealer_card2,dealer_card3,"\nthe dealers total is",total_dealer_card_value,"\nyou and the dealer got the same score, you keep your money")
        blackjack_total_money = blackjack_total_money + blackjack_bet
   
    if hit_stand_forfeit == "s":
        if total_card_value > 21:
            print("--------------------------------------------------------------------------- \nyour total went over 21, you lose £100")
            blackjack_bet=-100
        elif total_card_value > total_dealer_card_value:
            print("--------------------------------------------------------------------------- \nthe dealers cards are",dealer_card1,dealer_card2,dealer_card3,"\nthe dealers total is",total_dealer_card_value,"\nyou got a higher score than the derler, you win")
            blackjack_bet=blackjack_bet*2
        elif total_dealer_card_value >21:
            print("--------------------------------------------------------------------------- \nthe dealers cards are",dealer_card1,dealer_card2,dealer_card3,"\nthe dealers total is",total_dealer_card_value,"\nthe dealer went over 21, uou win")
            blackjack_bet=blackjack_bet*2
        elif total_dealer_card_value > total_card_value:
            print("--------------------------------------------------------------------------- \nthe dealers cards are",dealer_card1,dealer_card2,dealer_card3,"\nthe dealers total is",total_dealer_card_value,"\nthe dealer got a higher score than you, you lose £100")
        elif total_card_value == total_dealer_card_value:
             print("--------------------------------------------------------------------------- \nthe dealers cards are",dealer_card1,dealer_card2,dealer_card3,"\nthe dealers total is",total_dealer_card_value,"\nyou and the dealer got the same score, you keep your money")
        blackjack_total_money=blackjack_total_money + blackjack_bet
    if hit_stand_forfeit =="f":
            print("--------------------------------------------------------------------------- \nthe dealer keeps your money for forfeiting")
            blackjack_bet = blackjack_bet - blackjack_bet
            blackjack_total_money = blackjack_total_money + blackjack_bet
    print("your total amount is now",blackjack_total_money)
    print("press enter to play again or type (E) to exit blackjack")
    blackjack_end=input().lower()
    if blackjack_end == "e":
        print("your final tab was",blackjack_total_money)
        main()
    blackjack(blackjack_total_money)
def roulette_hub():
    print("Welcome to roulette \neven numbers = black \nodd number = red \n0 = green \nif you guess the correct number you win 3 times your bet \nif you guess the correct colour you win 1.5 times your bet \nif you lose on numbers you lose £10 but if you lose on colours you lose £100 \n---------------------------------------------------------------------------")
    roulette_total_money=0
    roulette(roulette_total_money)
def roulette(roulette_total_money):
    roulette_numbers=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)
    random_number=random.choice(roulette_numbers)
    print("how much would you like to bet?")
    roulette_bet=int(input("£"))
    print("would you like to bet on colours or numbers, type (C) for colours or (N) for numbers")
    bet_select=input().lower()
    if float(random_number) % 2 == 0:    
        roulette_colour = "black"
    elif float(random_number) == 0:
        roulette_colour = "green"
    else:
        roulette_colour = "red"
    if bet_select == "n":
        print("pick a number between 0-36")
        number_bet=input()
        if number_bet == random_number:
            print("the number was",random_number,"\nthe colour is",roulette_colour,"\nyou win")
            roulette_bet=roulette_bet*3
        else:
            print("the number was",random_number,"\nthe colour is",roulette_colour,"\nyou lose")
            roulette_bet=-10
    elif bet_select == "c":
        print("pick a colour,black(B),red(R),green(G)")
        colour_bet=input()
        if colour_bet == "b":
            colour_bet="black"
        if colour_bet == "r":
            colour_bet="red"
        if colour_bet == "g":
            colour_bet="green"
        if colour_bet == roulette_colour:
            print("the number was",random_number,"\nthe colour is",roulette_colour,"\nyou win")
            roulette_bet=roulette_bet*1.5
        else:
            print("the number was",random_number,"\nthe colour is",roulette_colour,"\nyou lose")
            roulette_bet=-10
    roulette_total_money=roulette_total_money+roulette_bet
    print("you total is now",roulette_total_money)
    print("press enter to play again or type (E) to leave roulette")
    roulette_end=input().lower()
    if roulette_end=="e":
        print("you final total was", roulette_total_money)
        main()
    roulette(roulette_total_money)
main()
