import new

print(new.logo)


dict={}
a=input("What is your name? :")
b=int(input("What is your bid?:"))


dict["Name"]=a
dict["Bid"]=[]
x=dict["Bid"]



for b in x:
    x.append(b)

print(x)


print(dict["Bid"])
c=input("Are there other bidders? Yes or no?").lower()
if c=="yes":
    clear()
elif c=="no":
    hscore = 0
    for dict["Bid"] in dict:
        if dict["Bid"] > hscore:
            hscore = dict["Bid"]
    print(dict[0])      
