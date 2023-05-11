# import the modules
from re import T, X
import data3
from data3 import data
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
print(resim.logo)
choose(a=x,b=y)
ed=input("Who has more followers? Type 'A' or 'B':")

should=True
while  should:    
    print(resim.logo)
    choose(a=x,b=y)
    ed=input("Who has more followers? Type 'A' or 'B':")
    rte=0
        
    if ed=="A":
        if cv>cv2:
            rte+=1
            print(f"Your count is {rte}")
            should=True
            choose(a=x,b=y)

        elif cv2>cv:
            print(f"Your guess is wrong.Try it again.")
            should=False
    elif ed== "B":
        if cv2>cv:                
            rte+=1
            print(f"Your count is {rte}")
            should=True
            choose(a=x,b=y)
        elif cv>cv2:
            print(f"Your guess is wrong.Try it again.")
            should=False
def EndF():
    print("fu")





