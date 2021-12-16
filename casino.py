import random
import time
WholeTotal=0
BlackjackTotalMoney=0
RouletteTotalMoney=0
def main():
    print("\nWelcome to my casino \nWould you like to play slots(S) blackjack(B) or roulette(R) (type(E)to exit)")
    GameSelect=input().lower()
    if GameSelect == "s":
        SlotsHub()
    if GameSelect == "b":
        BlackjackHub()
    if GameSelect == "r":
        RouletteHub()
    if GameSelect == "e":
        print("your final winning/loss are £",WholeTotal)
        time.sleep(1.5)
        exit()
    else:
        print("that's not an option")
        time.sleep(1)
        exit()
def SlotsHub():
    global WholeTotal
    print("welcome to the casino slots machines (it's £1 per go)")
    print("how much would you like to spend?")
    SlotsBet=float(input('£'))
    print("ok we will put that on your tab")
    time.sleep(1)
    WholeTotal=WholeTotal+SlotsBet
    while SlotsBet > 0:
        slots(SlotsBet)
def slots(SlotsBet):
    global WholeTotal
    SlotsNumbers=("7","420","69","911","666")
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
                WholeTotal=WholeTotal+50
               
    if (slots1) == "420":
        if slots2 == "420":
            if slots3 == "420":
                print("")
                print("tripple 420's here's £10")
                SlotsBet = SlotsBet + 10
                WholeTotal=WholeTotal+10
    if (slots1) == "69":
        if slots2 == "69":
            if slots3 == "69":
                print("")
                print("tripple 69's here's £10")
                SlotsBet = SlotsBet + 10
                WholeTotal = WholeTotal +10
    if (slots1) == "911":
        if slots2 == "911":
            if slots3 == "911":
                print("")
                print("tripple 911's here's £10")
                SlotsBet = SlotsBet + 10
                WholeTotal = WholeTotal + 10
    if (slots1) == "666":
        if slots2 == "666":
            if slots3 == "666":
                print("")
                print("tripple 666's here's £10")
                SlotsBet = SlotsBet + 10
                WholeTotal = WholeTotal + 10
    SlotsBet=SlotsBet-1
    WholeTotal=WholeTotal-1
    print("your current slots amount is £",SlotsBet)
    print("your total winnings/loss are £",WholeTotal)
    print("Press Enter to reroll or type (E) to leave slots")
    SlotsEnd=input().lower()
    print("")
    if SlotsEnd == "e":
        print("---------------------------------------------------------------------------")
        print("your final slots winnings are £", SlotsBet,"\nyour total winnings/loss are £", WholeTotal)
        main()
    if SlotsBet <= 1:
        print("---------------------------------------------------------------------------")
        print("\nyou are out of money sorry")
        main()
    slots(SlotsBet)
def BlackjackHub():
    print("--------------------------------------------------------------------------- \nwelcome to blackjack \n\nif you get a higher number than the dealer you win but if you get over 21 you lose \n\n1-10 = their coordinating number \nking, queen, jack = 10 \nace = 11 \nhit pulls another card into your hand \nstand keeps the cards you have in your hand \nforfeit ends the round(you lose your bet though)")
    blackjack()
def blackjack():
    global BlackjackTotalMoney
    global WholeTotal
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
    card5=random.choice(order)
    Card5Value=card5
    if card5 == "king":
        Card5Value=10
    if card5 == "queen":
        Card4Value=10
    if card5 == "jack":
        Card4Value=10
    if card5 == "ace":
        Card5Value=11
    TotalCardValue=(Card1Value+Card2Value)
     
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
    DealerCard4=random.choice(order)
    DealerCard4Value=DealerCard4
    if DealerCard4 == "king":
        DealerCard4Value=10
    if DealerCard4 == "queen":
        DealerCard4Value=10
    if DealerCard4 == "jack":
        DealerCard4Value=10
    if DealerCard4 == "ace":
        DealerCard4Value=11
    DealerCard5=random.choice(order)
    DealerCard5Value=DealerCard5
    if DealerCard5 == "king":
        DealerCard5Value=10
    if DealerCard5 == "queen":
        DealerCard5Value=10
    if DealerCard5 == "jack":
        DealerCard5Value=10
    if DealerCard5 == "ace":
        DealerCard5Value=11
    TotalDealerCardValue=(DealerCard1Value+DealerCard2Value)
    print("\nyour cards are",card1,card2,"\nyour total card value is",TotalCardValue) 
    print("\n\nthe dealers cards are",DealerCard1,"?")
    print("would you like to Hit(H), stand(S) or forfeit(F)")
    HitStandForfeit1=input().lower()
    if HitStandForfeit1 =="f":
        print("--------------------------------------------------------------------------- \nthe dealer keeps your money for forfeiting")
        BlackjackBet = BlackjackBet - BlackjackBet
        BlackjackTotalMoney = BlackjackTotalMoney + BlackjackBet
        WholeTotal = WholeTotal + BlackjackBet
        BlackJackEndHub()
    if HitStandForfeit1 == "s":
        print("--------------------------------------------------------------------------- \nthe dealers cards are now",DealerCard1,DealerCard2,"\nthe dealers total is now",TotalDealerCardValue)
        if TotalCardValue > 21:
            print("\nyour total went over 21, you lose £100")
            BlackjackBet=-100
        elif TotalCardValue > TotalDealerCardValue:
            print("\nyou got a higher score than the derler, you win")
            BlackjackBet=BlackjackBet*2
        elif TotalDealerCardValue >21:
            print("\nthe dealer went over 21, you win")
            BlackjackBet=BlackjackBet*2
        elif TotalDealerCardValue > TotalCardValue:
            print("\nthe dealer got a higher score than you, you lose £100")
            BlackjackBet=-100
        elif TotalCardValue == TotalDealerCardValue:
            print("\nyou and the dealer got the same score, you keep your money")
        BlackjackTotalMoney=BlackjackTotalMoney + BlackjackBet
        WholeTotal = WholeTotal + BlackjackBet
        BlackJackEndHub()
    if HitStandForfeit1 == "h":
        TotalCardValue= TotalCardValue + Card3Value 
        TotalDealerCardValue = TotalDealerCardValue + DealerCard3Value
        print("--------------------------------------------------------------------------- \nyour cards are now",card1,card2,card3,"\nyour total is now",TotalCardValue)
        print("--------------------------------------------------------------------------- \nthe dealers cards are now",DealerCard1,DealerCard2,DealerCard3,"\nthe dealers total is now",TotalDealerCardValue)
        if TotalCardValue > 21:
            print("--------------------------------------------------------------------------- \nyour total went over 21, you lose £100")
            BlackjackBet=-100
            BlackjackTotalMoney = BlackjackTotalMoney + BlackjackBet
            WholeTotal = WholeTotal + BlackjackBet
            BlackJackEndHub()
        elif TotalDealerCardValue >21:
            print("--------------------------------------------------------------------------- \nthe dealer went over 21, you win")
            BlackjackBet=BlackjackBet*2
            BlackjackTotalMoney = BlackjackTotalMoney + BlackjackBet
            WholeTotal = WholeTotal + BlackjackBet
            BlackJackEndHub()
        print("would you like to Hit(H), stand(S) or forfeit(F)")
        HitStandForfeit2=input().lower()
        if HitStandForfeit2 =="f":
            print("--------------------------------------------------------------------------- \nthe dealer keeps your money for forfeiting")
            BlackjackBet = BlackjackBet - BlackjackBet
            BlackjackTotalMoney = BlackjackTotalMoney + BlackjackBet
            WholeTotal = WholeTotal + BlackjackBet
            BlackJackEndHub()
        if HitStandForfeit2 == "s":
            if TotalCardValue > 21:
                print("--------------------------------------------------------------------------- \nyour total went over 21, you lose £100")
                BlackjackBet=-100
            elif TotalCardValue > TotalDealerCardValue:
                print("--------------------------------------------------------------------------- \nyou got a higher score than the derler, you win")
                BlackjackBet=BlackjackBet*2
            elif TotalDealerCardValue >21:
                print("--------------------------------------------------------------------------- \nthe dealer went over 21, you win")
                BlackjackBet=BlackjackBet*2
            elif TotalDealerCardValue > TotalCardValue:
                print("--------------------------------------------------------------------------- \nthe dealer got a higher score than you, you lose £100")
                BlackjackBet=-100
            elif TotalCardValue == TotalDealerCardValue:
                 print("--------------------------------------------------------------------------- \nyou and the dealer got the same score, you keep your money")
            BlackjackTotalMoney=BlackjackTotalMoney + BlackjackBet
            WholeTotal = WholeTotal + BlackjackBet
            BlackJackEndHub()
        if HitStandForfeit2 == "h":
            TotalCardValue= TotalCardValue + Card4Value 
            TotalDealerCardValue = TotalDealerCardValue + DealerCard4Value
            print("--------------------------------------------------------------------------- \nyour cards are now",card1,card2,card3,card4,"\nyour total is now",TotalCardValue)
            print("--------------------------------------------------------------------------- \nthe dealers cards are now",DealerCard1,DealerCard2,DealerCard3,DealerCard4,"\nthe dealers total is now",TotalDealerCardValue)
            if TotalCardValue > 21:
                print("--------------------------------------------------------------------------- \nyour total went over 21, you lose £100")
                BlackjackBet=-100
                BlackjackTotalMoney = BlackjackTotalMoney + BlackjackBet
                WholeTotal = WholeTotal + BlackjackBet
                BlackJackEndHub()
            elif TotalDealerCardValue >21:
                print("--------------------------------------------------------------------------- \nthe dealer went over 21, you win")
                BlackjackBet=BlackjackBet*2
                BlackjackTotalMoney = BlackjackTotalMoney + BlackjackBet
                WholeTotal = WholeTotal + BlackjackBet
                BlackJackEndHub()
            BlackjackTotalMoney=BlackjackTotalMoney + BlackjackBet
            WholeTotal = WholeTotal + BlackjackBet
            print("would you like to Hit(H), stand(S) or forfeit(F)")
            HitStandForfeit3=input().lower()
            if HitStandForfeit3 =="f":
                print("--------------------------------------------------------------------------- \nthe dealer keeps your money for forfeiting")
                BlackjackBet = BlackjackBet - BlackjackBet
                BlackjackTotalMoney = BlackjackTotalMoney + BlackjackBet
                WholeTotal = WholeTotal + BlackjackBet
                BlackJackEndHub()
            if HitStandForfeit3 == "s":
                if TotalCardValue > 21:
                    print("--------------------------------------------------------------------------- \nyour total went over 21, you lose £100")
                    BlackjackBet=-100
                elif TotalCardValue > TotalDealerCardValue:
                    print("--------------------------------------------------------------------------- \nyou got a higher score than the derler, you win")
                    BlackjackBet=BlackjackBet*2
                elif TotalDealerCardValue >21:
                    print("--------------------------------------------------------------------------- \nthe dealer went over 21, you win")
                    BlackjackBet=BlackjackBet*2
                elif TotalDealerCardValue > TotalCardValue:
                    print("--------------------------------------------------------------------------- \nthe dealer got a higher score than you, you lose £100")
                    BlackjackBet=-100
                elif TotalCardValue == TotalDealerCardValue:
                    print("--------------------------------------------------------------------------- \nyou and the dealer got the same score, you keep your money")
                BlackjackTotalMoney=BlackjackTotalMoney + BlackjackBet
                WholeTotal = WholeTotal + BlackjackBet
                BlackJackEndHub()
            if HitStandForfeit3 == "h":
                TotalCardValue= TotalCardValue + Card5Value 
                TotalDealerCardValue = TotalDealerCardValue + DealerCard5Value
                print("--------------------------------------------------------------------------- \nyour cards are now",card1,card2,card3,card4,card5,"\nyour total is now",TotalCardValue)
                print("--------------------------------------------------------------------------- \nthe dealers cards are now",DealerCard1,DealerCard2,DealerCard3,DealerCard4,DealerCard5,"\nthe dealers total is now",TotalDealerCardValue)
                if TotalCardValue > 21:
                    print("--------------------------------------------------------------------------- \nyour total went over 21, you lose £100")
                    BlackjackBet=-100
                elif TotalCardValue > TotalDealerCardValue:
                    print("--------------------------------------------------------------------------- \nyou got a higher score than the derler, you win")
                elif TotalDealerCardValue >21:
                    print("--------------------------------------------------------------------------- \nthe dealer went over 21, you win")
                    BlackjackBet=BlackjackBet*2
                elif TotalDealerCardValue > TotalCardValue:
                    print("--------------------------------------------------------------------------- \nthe dealer got a higher score than you, you lose £100")
                elif TotalCardValue == TotalDealerCardValue:
                    print("--------------------------------------------------------------------------- \nyou and the dealer got the same score, you keep your money")
                BlackjackTotalMoney = BlackjackTotalMoney + BlackjackBet
                WholeTotal = WholeTotal + BlackjackBet
                BlackJackEndHub()
def BlackJackEndHub():
    global BlackjackTotalMoney
    global WholeTotal
    print("your total blackjack winnings are £",BlackjackTotalMoney,"\nyour total winnings/loss are £",WholeTotal)
    print("press enter to play again or type (E) to exit blackjack")
    BlackjackEnd=input().lower()
    if BlackjackEnd == "e":
        print("your final blackjack winnings are £",BlackjackTotalMoney,"your total winnings/loss are £",WholeTotal)
        main()
    blackjack()
def RouletteHub():
    print("Welcome to roulette \neven numbers = black \nodd number = red \n0 = green \nif you guess the correct number you win 3 times your bet \nif you guess the correct colour you win 1.5 times your bet \nif you lose on numbers you lose £10 but if you lose on colours you lose £100 \n---------------------------------------------------------------------------")
    roulette()
def roulette():
    global RouletteTotalMoney
    global WholeTotal
    RouletteNumbers=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)
    RandomNumber=random.choice(RouletteNumbers)
    print("how much would you like to bet?")
    RouletteBet=int(input("£"))
    print("would you like to bet on colours or numbers, type (C) for colours or (N) for numbers")
    BetSelect=input().lower()
    if float(RandomNumber) % 2 == 0:    
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
    WholeTotal = WholeTotal + RouletteBet
    print("you total roulette winnings/loss are £",RouletteTotalMoney,"\nyour total winnings/loss are £",WholeTotal)
    print("press enter to play again or type (E) to leave roulette")
    roulette_end=input().lower()
    if roulette_end=="e":
        print("you final roulette winnings/loss are £", RouletteTotalMoney,"\nyour total winnings/loss are £",WholeTotal )
        main()
    roulette()
main()
