import random
import time

MoneyEarnt = 0

def Main():
    print("Welcome to the casino, would u like to play slots(S), blackjack(B) or roulette (R)")
    GameSelector = input().lower()
    if GameSelector == "s":
        StartSlots()
    if GameSelector == "b" :
        BlackJack()
    if GameSelector == "r":
        pass
    
def StartSlots():
    print("Welcome to the casino slots machines (it's £1 per go) \n How much would you like to spend?")
    BetMoney=float(input('£')) 
    print("Ok, that value is now tab.")
    time.sleep(1)
    Slots(BetMoney)

def Slots(BetMoney):
    global MoneyEarnt
    while True:
        SlotMachine = [7,420,69,666,911]
        MoneyEarnt = BetMoney
        while float(MoneyEarnt) > 0:
            RandomMoney = [random.choice(SlotMachine) for i in range(3)]
            print(RandomMoney[0],RandomMoney[1],RandomMoney[2])
            if (RandomMoney[0]) == SlotMachine[0]:
                if RandomMoney[1] == SlotMachine[0]:
                    if RandomMoney[2] == SlotMachine[0]:
                        print("\ntripple 7's here's £50")
                        MoneyEarnt = MoneyEarnt + 50

            if (RandomMoney[0]) == SlotMachine[1]:
                if RandomMoney[1] == SlotMachine[1]:
                    if RandomMoney[2] == SlotMachine[1]:
                        print("\ntripple 420's here's £10")
                        MoneyEarnt = MoneyEarnt + 10

            if (RandomMoney[0]) == SlotMachine[2]:
                if RandomMoney[1] == SlotMachine[2]:
                    if RandomMoney[2] == SlotMachine[2]:
                        print("\ntripple 69's here's £10")
                        MoneyEarnt = MoneyEarnt + 10

            if (RandomMoney[0]) == SlotMachine[3]:
                if RandomMoney[1] == SlotMachine[3]:
                    if RandomMoney[2] == SlotMachine[3]:
                        print("\ntripple 666's here's £10")
                        MoneyEarnt = MoneyEarnt + 10

            if (RandomMoney[0]) == SlotMachine[4]:
                if RandomMoney[1] == SlotMachine[4]:
                    if RandomMoney[2] == SlotMachine[4]:
                        print("\ntripple 911's here's £10")
                        MoneyEarnt = MoneyEarnt + 10

            MoneyEarnt=MoneyEarnt-1
            print("our current balance is £",MoneyEarnt)
            print("Press Enter to reroll or exit to leave")
            l=input()
            if l == "exit":
                Main()
            Slots(MoneyEarnt)
        print("You are out of money sorry")
        MoneyEarnt = 0
        time.sleep(2)
        Main()

def BlackJack():
    while (aaa) == 2:
        bet2=0
        kp=1
        bet3=bet2
        print("---------------------------------------------------------------------------")
        print("welcome to blackjack")
        print()
        print("if you get MoneyEarnt higher number than the dealer you win but if you get over 21 you lose")
        print()
        print("1-10 = their coordinating number")
        print("king, queen, jack = 10")
        print("ace = 11")
        print("hit pulls another card into your hand")
        print("stand keeps the cards you have in your hand")
        print("forfeit ends the round(you lose your bet though)")
        while kp > 0:
            a1=1
            a2=2
            a3=3
            a4=4
            a5=5
            a6=6
            a7=7
            a8=8
            a9=9
            a10=10
            king="king"
            queen="queen"
            jack="jack"
            ace="ace"
            order=(a1,a1,a1,a1,a2,a2,a2,a2,a3,a3,a3,a3,a4,a4,a4,a4,a5,a5,a5,a5,a6,a6,a6,a6,a7,a7,a7,a7,a8,a8,a8,a8,a9,a9,a9,a9,a10,a10,a10,a10,king,king,king,king,queen,queen,queen,queen,jack,jack,jack,jack,ace,ace,ace,ace)
            print("---------------------------------------------------------------------------")
            print("what is your bet")
            bet1=float(input("£"))
            go=input("press enter to get your numbers")
            d1=random.choice(order)
            od1=d1
            ood1=od1
            if od1 == ace:
                od1 = 11
            if od1 == king:
                od1 = 10
            if od1 == queen:
                od1 = 10
            if od1 == jack:
                od1 = 10
            d2=random.choice(order)
            od2=d2
            ood2=od2
            if od2 == ace:
                od2 = 11
            if od2 == king:
                od2 = 10
            if od2 == queen:
                od2 = 10
            if od2 == jack:
                od2 = 10
            d3=random.choice(order)
            od3=d3
            ood3=od3
            if od3 == ace:
                od3 = 11
            if od3 == king:
                od3 = 10
            if od3 == queen:
                od3 = 10
            if od3 == jack:
                od3 = 10
            total1=(od1+od2+od3)

            
            de1=random.choice(order)
            oed1=de1
            ooed1=oed1
            if oed1 == ace:
                oed1 = 11
            if oed1 == king:
                oed1 = 10
            if oed1 == queen:
                oed1 = 10
            if oed1 == jack:
                oed1 = 10
            de2=random.choice(order)
            oed2=de2
            ooed2=oed2
            if oed2 == ace:
                oed2 = 11
            if oed2 == king:
                oed2 = 10
            if oed2 == queen:
                oed2 = 10
            if oed2 == jack:
                oed2 = 10
            de3=random.choice(order)
            oed3=de3
            ooed3=oed3
            if oed3 == ace:
                oed3 = 11
            if oed3 == king:
                oed3 = 10
            if oed3 == queen:
                oed3 = 10
            if oed3 == jack:
                oed3 = 10
            print()
            print("---------------------------------------------------------------------------")
            total2=(oed1+oed2+oed3)
            print()
            print("your cards are",ooed1,ooed2,ooed3)
            print("your total is",total2)
            print()
            print("dealers cards",ood1,"?","?")
            print()
            print("would you like to Hit(RandomMoney[0]), stand(S) or forfeit(SlotMachine[4])")
            ask1=input().upper()
            if ask1 == "RandomMoney[0]":
                SHD1=random.choice(order)
                SHO1=SHD1
                eooed1=SHO1
                if SHO1 == ace:
                    SHO1 = 11
                if SHO1 == king:
                    SHO1 = 10
                if SHO1 == queen:
                    SHO1 = 10
                if SHO1 == jack:
                    SHO1
                total2=(oed1+oed2+oed3+SHO1)
                print("your cards are now",ooed1,ooed2,ooed3,SHO1)
                print("your total is now",total2)
                print("---------------------------------------------------------------------------")
                if total2 > 21:
                    print("your total went over 21, you  now lose £100")
                    bet1=bet1-bet1-100
                elif total2 > total1:
                    print("you win")
                    bet1=bet1*2
                elif total1>21:
                    print("the dealers cards were",ood1,ood2,ood3)
                    print("the dealers total was",total1)
                    print()
                    print("the dealer got over 21, you win")
                    bet1=bet1*2
                elif total1>total2:
                    print("the dealers cards were",ood1,ood2,ood3)
                    print("the dealers total was",total1)
                    print()
                    print("the dealer had higher numbers, you now lose £100")
                    bet1=bet1-bet1-100
                elif total2 == total1:
                    print("the dealers cards were",ood1,ood2,ood3)
                    print("the dealers total was",total1)
                    print()
                    print("you and the dealer got the same score,you keep your money")
                    bet1=bet1
                print("press enter to play again or type exit to leave")
                end=input()
                if end == "exit":
                    kp = kp-1

            if ask1 == "S":
                if total2 > 21:
                    print("---------------------------------------------------------------------------")
                    print("your total went over 21, you lost, you now lose £100")
                    bet1=bet1-bet1-100
                elif total2 > total1:
                    print("---------------------------------------------------------------------------")
                    print("you got higher numbers than the dealer, you win")
                    bet1=bet1*2
                elif total1>21:
                    print("---------------------------------------------------------------------------")
                    print("the dealers cards were",ood1,ood2,ood3)
                    print("the dealers total was",total1)
                    print()
                    print("the dealer got over 21, you win")
                    bet1=bet1*2
                elif total1>total2:
                    print("---------------------------------------------------------------------------")
                    print("the dealers cards were",ood1,ood2,ood3)
                    print("the dealers total was",total1)
                    print()
                    print("the dealer had higher numbers, you now lose £100")
                    bet1=bet1-bet1-100
                elif total2 == total1:
                    print("---------------------------------------------------------------------------")
                    print("the dealers cards were",ood1,ood2,ood3)
                    print("the dealers total was",total1)
                    print()
                    print("you and the dealer got the same score,you keep your money")
                    bet1=bet1

            if ask1 =="SlotMachine[4]":
                print("---------------------------------------------------------------------------")
                print("the dealer keeps your money for forfeiting")
                bet1=bet1-bet1
                
            bet2=bet2+bet1
            print("your total tab is now",bet2)
            print("press enter to play again or exit to leave")
            end=input()
            if end == "exit":
                kp = kp-1
        input("enter to end")
        aaa = aaa - 2
    total3=0

# def Roulette():   
#     while aaa == 3:
#         bor="0"
#         colour="0"
#         NumsUpToThirtySeven=[i for i in range(0,36)]
#         print("welcome to roulette")
#         print("the rules are simple")
#         print("if you guess the colour or number you win if you guess wrong you lose")
#         print("if you pick the correct numbers your bet gets timesed by 3")
#         print("if you pick the correct colour your bet gets timesed by 2 ")
#         print("if you lose on colours you lose 10 but if you lose on colours you lose 100")
#         print("---------------------------------------------------------------------------")
#         print("how much money do you want to bet")
#         SlotMachine[1]=input("£")
#         bet=SlotMachine[1]
#         print("black = even numbers  red = odd numbers  0 = green")
#         print("would you like to bet on numbers(N) or colours(SlotMachine[1])")
#         print("---------------------------------------------------------------------------")
#         SlotMachine[3]=input().lower()
#         if SlotMachine[3] == "n":
#             print("what number would you like between 0-36")
#             SlotMachine[4]=int(input())
#             SlotMachine[2]= random.choice(SlotMachine[0])
#             num=SlotMachine[2]
#             if int(SlotMachine[2]) % 2 == 0:    #if SlotMachine[2] divided by 2 is equal to 0 (% means divide)
#                 bor = "black"
#             elif int(SlotMachine[2]) == MoneyEarnt:
#                 bor = "green"
#             else:
#                 bor = "red"
#             print("the number is",num)
#             print("the colour is", bor)
#             if SlotMachine[4] == num:
#                 print("you win")
#                 bet4 = int(bet4)*3
#             else:
#                 print("your number was not correct, you lost")
#                 bet4 = -10
#         if SlotMachine[3] =="SlotMachine[1]":
#             print("Which colour would you like black(SlotMachine[0]) red(R) or green(G)")
#             g=input().lower()
#             RandomNumChoice = random.choice(SlotMachine[0])
#             num1 = RandomNumChoice
#             if float(num1) % 2 == 0:    #if SlotMachine[2] divided by 2 is equal to 0 (% means divide)
#                 bor = "black"
#             elif float(num1) == MoneyEarnt:
#                 bor = "green"
#             else:
#                 bor = "red"
#             if g == "SlotMachine[0]":
#                 colour = "black"
#             elif g == "r":
#                 colour = "red"
#             elif g == "g":
#                 colour = "green"           
#             print("the number is",num1)
#             print("the colour is", bor)
#             if colour == bor:
#                 print("you win")
#                 bet4 = int(bet4)*2
#             else:
#                 print("your colour wasn't correct, you lost")
#                 bet4 = -100
#         total3=total3+bet4
#         print("your new total is",total3)
#         print("press enter to play again or type exit to leave")
#         end=input().lower()
#         if end == "exit":
#             Main()
        

Main()
