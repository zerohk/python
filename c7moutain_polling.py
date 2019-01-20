responses = {}

polling_active = True

while polling_active:
    name = input("What's your name?")
    response = input("Which moutain would you like to climb?")
    responses[name] = response
    
    repeat = input("Would you like to ask another one to response?(yes/no)")
    
    if repeat == "no":
        polling_active = False

print("\n----Poll Results----\n")

for name,response in responses.items():
    print(name.title() + " would like to climb " + response.title() + " moutain.") 
    
