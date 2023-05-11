#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from deneme import logo
print(logo)

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!Welcome to the Number Guessing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

numbers=[]
n=0
for n in range (0,100):
    n+=1
    numbers.append(n)
    l=list(map(int,numbers))
a = random.choice(l)


 

def hard(c):
    t=0
    while t<4:
        c=int(input("Guess a number: "))
        
        if c < a:
            print("Too low.")          
            t+=1
            u=4-t
            print(f"You have {u} turns.")
            if t==4 and u==0:
                print("You didn't make it.") 
        elif c > a:
            print ("Too high.")
            t+=1
            u=4-t
            print(f"You have {u} turns.")
            if t==4 and u==0:
                print("You didn't make it.")     
        elif c == a:
            print(f"You won.CPU guessed {a}")
        
            

 
def easy(z):
    
    m=0
    while m<9:
        z=int(input("Guess a number: "))    
        if z < a:
            print("Too low.")
            m+=1
            y=9-m
            print(f"You have {y} turns.")
            if m==9 and y==0:
                print("You didn't make it.") 
        elif z > a:
            print ("Too high.")
            m+=1
            y=9-m
            print(f"You have {y} turns.")
            if m==9 and y==0:
                print("You didn't make it.")    
        elif z == a:
            print(f"You won.CPU guessed {a}")


b=input("Which mode do you want to play? Type 'e' for easy mode,'h' for hard mode: ").lower()
x=int(input("Guess a number: "))

if b=="e":
    
    
    if x < a:
        print("Too low.")
        print("You have 9 turns.")
    elif x > a:
        print ("Too high.")
        print("You have 9 turns.")
    elif x == a:
        print(f"You won.CPU guessed {a}")
    easy(z=x)
elif b=="h":
    if x < a:
        print("Too low.")
        print("You have 4 turns.")
    elif x > a:
        print ("Too high.")
        print("You have 4 turns.")
    elif x == a:
        print(f"You won.CPU guessed {a}")
    hard(c=x)        
