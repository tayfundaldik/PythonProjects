import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
x=input("Do you want to play a game of Blackjack?\nType 'y' or 'n':\n").lower()
player1= random.sample(cards,2)

print(f"You have {player1}")
dealer=random.sample(cards,2)

print(f"Dealer has {dealer}")

def add(a,b):
    return a+b

i=0
o=0
for n in range(0,len(player1)-1): 
    i=add(a=player1[0],b=player1[1]) 
    j= add(a=i,b=player1[n])



    o= add(a=dealer[0],b=dealer[1])
    u= add(a=o,b=dealer[n])


if x== "y":
    should_continue=True
    while  should_continue :
        z=input("Do you want another card?Type 'y' or 'n': ").lower()

        if  z=="y":
            player1.append(random.choice(cards))
            print(f"You have {player1}")
            dealer.append(random.choice(cards))
            if j>21 : 
                if u<21 or u==21:
                    print(f"You lost the game.Dealer had {dealer}.")
                else:
                    print(f"The game is draw.Dealer had {dealer}.")
            elif j==21:
                if u>21 or u<21:
                    print(f"You won. Dealer had {dealer}")
                else:
                    print(f"The game is draw.Dealer had {dealer}.")
            else:
                if (u <21 and u>j) or u==21:
                    print(f"You lost the game.Dealer had {dealer}.")
                elif u<21 and j>u:
                    print(f"You won. Dealer had {dealer}")
                else:
                    print(f"You lost the game.Dealer had {dealer}.")



        elif z=="n":
            should_continue=False

elif x=="n":
    print("Okay...")