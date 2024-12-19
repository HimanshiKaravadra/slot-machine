#slot machine
import random
symbols = ["$","&","£","*","%"]

while True :
    tokens = 100
    print("welcome to slot machine game")
    print("Let's go gambling!!")
    while tokens > 0 :
        print("you have", tokens, "tokens")
        try :
            bet = int(input("enter bet amount: "))
        except:
            print("enter a valid number of tokens")
            continue
        if bet > tokens:
            print("not enough tokens")
        else:
            tokens-= bet
            sqr1 = random.choice(symbols)
            sqr2 = random.choice(symbols)
            sqr3 = random.choice(symbols)

            print()

            print("|", random.choice(symbols), "|", random.choice(symbols), "|", random.choice(symbols), "|")
            print("-------------")

            print("|", sqr1, "|", sqr2, "|", sqr3, "|")
            print("-------------")

            print("|", random.choice(symbols), "|", random.choice(symbols), "|", random.choice(symbols), "|")
            print()

            if sqr1 == sqr2 == sqr3 :
                won_money = bet*2
                print("you won", won_money,"tokens")
                tokens += won_money
            else :
                print("you lost this time:( ")
    print("you ran out of tokens")
    print("better luck next time")
    print()


