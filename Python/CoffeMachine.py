from importlib import resources
import dataque

latte=dataque.MENU["latte"]
espresso=dataque.MENU["espresso"]
cappuccino=dataque.MENU["cappuccino"]


global dif1,dif2,dif3
global s
should=True
#espresso[ingredients]
def check(b):
    dif1=dataque.resources["water"]-b["ingredients"]["water"]
    dif2=dataque.resources["milk"]-b["ingredients"]["milk"]
    dif3=dataque.resources["coffee"]-b["ingredients"]["coffee"]
    
  
    
    if dif1<b["ingredients"]["water"] and dif2<b["ingredients"]["milk"] and dif3<b["ingredients"]["coffee"]:
        print("Sorry not enough resources...")
    elif dif1<b["ingredients"]["water"] and dif2>b["ingredients"]["milk"] and dif3>b["ingredients"]["coffee"]:    
        print("Sorry not enough water...")
    elif dif1>b["ingredients"]["water"] and dif2<b["ingredients"]["milk"] and dif3>b["ingredients"]["coffee"]:    
        print("Sorry not enoug milk...")
    elif dif1>b["ingredients"]["water"] and dif2>b["ingredients"]["milk"] and dif3<b["ingredients"]["coffee"]:    
        print("Sorry not enough coffee...")

def rep():
    dataque.resources["water"]-=choice["ingredients"]["water"]
    dataque.resources["milk"] -= choice["ingredients"]["milk"]
    dataque.resources["coffee"] -= choice["ingredients"]["coffee"]
    
    print(res1,res2,res3)

global x,y,z,t
def coin(xt,yt,zt,tt):
    
    return xt+yt+zt+tt

global res1,res2,res3
def check2():
    ab=coin(xt=x,yt=y,zt=z,tt=t)
    cd=choice["cost"]
    if ab>cd:
        xc=ab-cd
        print(f"Here is your ${xc} change.")
        
    elif ab<cd:
        print("Sorry that's not enough money.Your money is refunded.")    

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

while should:
    
    choice=input("What would you like? (espresso/latte/cappuccino):").lower()
    drink = choice
    if choice =="latte":
        s=choice
        choice=latte
        pen=int(input ("Quarters please (Count): "))
        ten=int(input("Dimes please (Count): "))
        cen=int(input("Nickels please (Count): "))
        men=int(input("Pennies please (Count):"))
        x=pen* 0.25
        y=ten*0.1
        z=cen*0.05
        t=men*0.01
        check(b=choice)
        check2()
        make_coffee(drink_name=choice, order_ingredients=drink["ingredients"])
    elif choice == "espresso":
        s=choice
        choice=espresso
        pen=int(input ("Quarters please (Count): "))
        ten=int(input("Dimes please (Count): "))
        cen=int(input("Nickels please (Count): "))
        men=int(input("Pennies please (Count):"))
        x=pen* 0.25
        y=ten*0.1
        z=cen*0.05
        t=men*0.01
        check(b=choice)
        check2()
        make_coffee(choice, drink["ingredients"])
    elif choice == "cappuccino":
        s=choice
        choice=cappuccino
        pen=int(input ("Quarters please (Count): "))
        ten=int(input("Dimes please (Count): "))
        cen=int(input("Nickels please (Count): "))
        men=int(input("Pennies please (Count):"))
        x=pen* 0.25
        y=ten*0.1
        z=cen*0.05
        t=men*0.01
        check(b=choice)
        check2()
        make_coffee(choice, drink["ingredients"])
    elif choice =="report":
        print(f"Water: {dataque.resources['water']}ml")
        print(f"Milk: {dataque.resources['milk']}ml")
        print(f"Coffee: {dataque.resources['coffee']}g")
        
    elif choice =="off":
        should=False