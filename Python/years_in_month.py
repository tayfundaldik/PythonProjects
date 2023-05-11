# import the modules
from re import X
import data
from data import data
import random
import resim


ed=""
x=""
y=""
yt=0
tr=0
def choose(a,b):
    a=random.choice(data)
    b=random.choice(data)
    if a==b:
        a=random.choice(data)
        b=random.choice(data)
    global cv,cv2
    cv=int(a["follower_count"])
    cv2=int(b["follower_count"])
    print(a["name"],a["description"],a["country"])
    print(resim.vs)
    print(b["name"],b["description"],b["country"])
    ed=input("Who has more followers? Type 'A' or 'B'")
    compare(a=cv,b=cv2,ed=ed)

    

def compare(a,b,ed):
    
    if a>b:
        i=0
        cont=True
        while cont is not True:
           # ed=input("Who has more followers? Type 'A' or 'B'")
            i+=1
            if ed=="A":
                choose(a=x,b=y)
                print(f"Your count is {i}")
            elif ed=="B"  :
                choose(a=x,b=y)
                print(f"Your guess is wrong.Try it again.")
                EndF()
                cont=False
    elif b>a:
        i=0
        cont=True
        while cont is not True:
            
            #ed=input("Who has more followers? Type 'A' or 'B'")
            i+=1
            if ed=="B":
                choose(a=x,b=y)
                print(f"Your count is {i}")
            elif ed=="A"  :
                choose(a=x,b=y)
                print(f"Your guess is wrong.Try it again.")
                EndF()
                cont=False

def EndF():
    print("fu")

print(resim.logo)
choose(a=x,b=y)


