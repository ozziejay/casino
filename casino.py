import random
import time
def main():
    print("\nWelcome to my casino \nWould you like to play slots(S) blackjack(B) or roulette(R)")
    GameSelect=input().lower()
    if GameSelect == "s":
        SlotsHub()
    if GameSelect == "b":
        BlackjackHub()
    if GameSelect == "r":
        RouletteHub()
    else:
        print("that's not a game option")
        time.sleep(1)
        exit()
def SlotsHub():
    print("welcome to the casino slots machines (it's £1 per go)")
    print("how much would you like to spend?")
    SlotsBet=float(input('£'))
    print("ok we will put that on your tab")
    time.sleep(1)
    while SlotsBet > 0:
        slots(SlotsBet)
def slots(SlotsBet):
    SlotsNumbers=("7","7","7","420","420","420","69","69","69","911","911","911","666","666","666")
    slots1=random.choice(SlotsNumbers)
    slots2=random.choice(SlotsNumbers)
    slots3=random.choice(SlotsNumbers)
    print(slots1,slots2,slots3)
    if (slots1) == "7":
        if slots2 == "7":
            if slots3 == "7":
                print("")
                print("tripple 7's here's £50")
                SlotsBet = SlotsBet + 50
    if (slots1) == "420":
        if slots2 == "420":
            if slots3 == "420":
                print("")
                print("tripple 420's here's £10")
                SlotsBet = SlotsBet + 10
    if (slots1) == "69":
        if slots2 == "69":
            if slots3 == "69":
                print("")
                print("tripple 69's here's £10")
                SlotsBet = SlotsBet + 10
    if (slots1) == "911":
        if slots2 == "911":
            if slots3 == "911":
                print("")
                print("tripple 666's here's £10")
                SlotsBet = SlotsBet + 10
    if (slots1) == "666":
        if slots2 == "666":
            if slots3 == "666":
                print("")
                print("tripple 911's here's £10")
                SlotsBet = SlotsBet + 10
    SlotsBet=SlotsBet-1
    print("your current balance is £",SlotsBet)
    print("Press Enter to reroll or type (E) to leave slots")
    SlotsEnd=input().lower()
    print("")
    if SlotsEnd == "e":
        print("---------------------------------------------------------------------------")
        print("your final tab was £", SlotsBet)
        main()
    if SlotsBet <= 1:
        print("---------------------------------------------------------------------------")
        print("\nyou are out of money sorry")
        main()
    slots(SlotsBet)

def BlackjackHub():
    BlackjackTotalMoney=0
    print("--------------------------------------------------------------------------- \nwelcome to blackjack \n\nif you get a higher number than the dealer you win but if you get over 21 you lose \n\n1-10 = their coordinating number \nking, queen, jack = 10 \nace = 11 \nhit pulls another card into your hand \nstand keeps the cards you have in your hand \nforfeit ends the round(you lose your bet though)")
    blackjack(BlackjackTotalMoney)
def blackjack(BlackjackTotalMoney):
    TotalCardValue=0
    TotalDealerCardValue=0
    order=(1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'king','king','king','king','queen','queen','queen','queen','jack','jack','jack','jack','ace','ace','ace','ace')
    print("--------------------------------------------------------------------------- \nwhat is your bet")
    BlackjackBet=float(input("£"))
    input("press enter to get your cards")
    card1=random.choice(order)
    Card1Value=card1
    if card1 == "king":
        Card1Value=10
    if card1 == "queen":
        Card1Value=10
    if card1 == "jack":
        Card1Value=10
    if card1 == "ace":
        Card1Value=11
    card2=random.choice(order)
    Card2Value=card2
    if card2 == "king":
        Card2Value=10
    if card2 == "queen":
        Card2Value=10
    if card2 == "jack":
        Card2Value=10
    if card2 == "ace":
        Card2Value=11
    card3=random.choice(order)
    Card3Value=card3
    if card3 == "king":
        Card3Value=10
    if card3 == "queen":
        Card3Value=10
    if card3 == "jack":
        Card3Value=10
    if card3 == "ace":
        Card3Value=11
    TotalCardValue=(Card1Value+Card2Value+Card3Value)

    DealerCard1=random.choice(order)
    DealerCard1Value=DealerCard1
    if DealerCard1 == "king":
        DealerCard1Value=10
    if DealerCard1 == "queen":
        DealerCard1Value=10
    if DealerCard1 == "jack":
        DealerCard1Value=10
    if DealerCard1 == "ace":
        DealerCard1Value=11
    DealerCard2=random.choice(order)
    DealerCard2Value=DealerCard2
    if DealerCard2 == "king":
        DealerCard2Value=10
    if DealerCard2 == "queen":
        DealerCard2Value=10
    if DealerCard2 == "jack":
        DealerCard2Value=10
    if DealerCard2 == "ace":
        DealerCard2Value=11
    DealerCard3=random.choice(order)
    DealerCard3Value=DealerCard3
    if DealerCard3 == "king":
        DealerCard3Value=10
    if DealerCard3 == "queen":
        DealerCard3Value=10
    if DealerCard3 == "jack":
        DealerCard3Value=10
    if DealerCard3 == "ace":
        DealerCard3Value=11
    TotalDealerCardValue=(DealerCard1Value+DealerCard2Value+DealerCard3Value)
    print("\nyour cards are",card1,card2,card3,"\nyour total card value is",TotalCardValue) 
    print("\n\nthe dealers cards are",DealerCard1,"?","?")
    print("would you like to Hit(H), stand(S) or forfeit(F)")
    HitStandForfeit=input().lower()
    if HitStandForfeit == "h":
        card4=random.choice(order)
        Card4Value=card4
        if card4 == "king":
            Card4Value=10
        if card4 == "queen":
            Card4Value=10
        if card4 == "jack":
            Card4Value=10
        if card4 == "ace":
            Card4Value=11
        TotalCardValue=(TotalCardValue+Card4Value)
        print("--------------------------------------------------------------------------- \nyour cards are now",card1,card2,card3,card4,"\nyour total is now",TotalCardValue)
        if TotalCardValue > 21:
            print("--------------------------------------------------------------------------- \nyour total went over 21, you lose £100")
            BlackjackBet=-100
        elif TotalCardValue > TotalDealerCardValue:
            print("--------------------------------------------------------------------------- \nthe dealers cards are",DealerCard1,DealerCard2,DealerCard3,"\nthe dealers total is",TotalDealerCardValue,"\nyou got a higher score than the derler, you win")
            BlackjackBet=BlackjackBet*2
        elif TotalDealerCardValue >21:
            print("--------------------------------------------------------------------------- \nthe dealers cards are",DealerCard1,DealerCard2,DealerCard3,"\nthe dealers total is",TotalDealerCardValue,"\nthe dealer went over 21, uou win")
            BlackjackBet=BlackjackBet*2
        elif TotalDealerCardValue > TotalCardValue:
            print("--------------------------------------------------------------------------- \nthe dealers cards are",DealerCard1,DealerCard2,DealerCard3,"\nthe dealers total is",TotalDealerCardValue,"\nthe dealer got a higher score than you, you lose £100")
        elif TotalCardValue == TotalDealerCardValue:
             print("--------------------------------------------------------------------------- \nthe dealers cards are",DealerCard1,DealerCard2,DealerCard3,"\nthe dealers total is",TotalDealerCardValue,"\nyou and the dealer got the same score, you keep your money")
        BlackjackTotalMoney = BlackjackTotalMoney + BlackjackBet
   
    if HitStandForfeit == "s":
        if TotalCardValue > 21:
            print("--------------------------------------------------------------------------- \nyour total went over 21, you lose £100")
            BlackjackBet=-100
        elif TotalCardValue > TotalDealerCardValue:
            print("--------------------------------------------------------------------------- \nthe dealers cards are",DealerCard1,DealerCard2,DealerCard3,"\nthe dealers total is",TotalDealerCardValue,"\nyou got a higher score than the derler, you win")
            BlackjackBet=BlackjackBet*2
        elif TotalDealerCardValue >21:
            print("--------------------------------------------------------------------------- \nthe dealers cards are",DealerCard1,DealerCard2,DealerCard3,"\nthe dealers total is",TotalDealerCardValue,"\nthe dealer went over 21, uou win")
            BlackjackBet=BlackjackBet*2
        elif TotalDealerCardValue > TotalCardValue:
            print("--------------------------------------------------------------------------- \nthe dealers cards are",DealerCard1,DealerCard2,DealerCard3,"\nthe dealers total is",TotalDealerCardValue,"\nthe dealer got a higher score than you, you lose £100")
        elif TotalCardValue == TotalDealerCardValue:
             print("--------------------------------------------------------------------------- \nthe dealers cards are",DealerCard1,DealerCard2,DealerCard3,"\nthe dealers total is",TotalDealerCardValue,"\nyou and the dealer got the same score, you keep your money")
        BlackjackTotalMoney=BlackjackTotalMoney + BlackjackBet
    if HitStandForfeit =="f":
            print("--------------------------------------------------------------------------- \nthe dealer keeps your money for forfeiting")
            BlackjackBet = BlackjackBet - BlackjackBet
            BlackjackTotalMoney = BlackjackTotalMoney + BlackjackBet
    print("your total amount is now",BlackjackTotalMoney)
    print("press enter to play again or type (E) to exit blackjack")
    BlackjackEnd=input().lower()
    if BlackjackEnd == "e":
        print("your final tab was",BlackjackTotalMoney)
        main()
    blackjack(BlackjackTotalMoney)
def RouletteHub():
    print("Welcome to roulette \neven numbers = black \nodd number = red \n0 = green \nif you guess the correct number you win 3 times your bet \nif you guess the correct colour you win 1.5 times your bet \nif you lose on numbers you lose £10 but if you lose on colours you lose £100 \n---------------------------------------------------------------------------")
    RouletteTotalMoney=0
    roulette(RouletteTotalMoney)
def roulette(RouletteTotalMoney):
    RouletteNumbers=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)
    RandomNumber=random.choice(RouletteNumbers)
    print("how much would you like to bet?")
    RouletteBet=int(input("£"))
    print("would you like to bet on colours or numbers, type (C) for colours or (N) for numbers")
    BetSelect=input().lower()
    if float(RandomNumber) % 2 == 0:    #if d divided by 2 is equal to 0 (% means divide)
        RouletteColour = "black"
    elif float(RandomNumber) == 0:
        RouletteColour = "green"
    else:
        RouletteColour = "red"
    if BetSelect == "n":
        print("pick a number between 0-36")
        NumberBet=input()
        if NumberBet == RandomNumber:
            print("the number was",RandomNumber,"\nthe colour is",RouletteColour,"\nyou win")
            RouletteBet=RouletteBet*3
        else:
            print("the number was",RandomNumber,"\nthe colour is",RouletteColour,"\nyou lose")
            RouletteBet=-10
    elif BetSelect == "c":
        print("pick a colour,black(B),red(R),green(G)")
        ColourBet=input()
        if ColourBet == "b":
            ColourBet="black"
        if ColourBet == "r":
            ColourBet="red"
        if ColourBet == "g":
            ColourBet="green"
        if ColourBet == RouletteColour:
            print("the number was",RandomNumber,"\nthe colour is",RouletteColour,"\nyou win")
            RouletteBet=RouletteBet*1.5
        else:
            print("the number was",RandomNumber,"\nthe colour is",RouletteColour,"\nyou lose")
            RouletteBet=-10
    RouletteTotalMoney=RouletteTotalMoney+RouletteBet
    print("you total is now",RouletteTotalMoney)
    print("press enter to play again or type (E) to leave roulette")
    roulette_end=input().lower()
    if roulette_end=="e":
        print("you final total was", RouletteTotalMoney)
        main()
    roulette(RouletteTotalMoney)
main()
