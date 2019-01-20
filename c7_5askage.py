ask = "How old are you?  "

age = " "

while age:
    age = input(ask)
    
    if age == "quit":
        break
    if int(age) < 3:
        print("You are free!")
    elif int(age) >=3 and int(age) < 12:
        print("You need to pay $10")
    else:
        print("You need to pay $15")

