hint = "If you could visit one place in the world, where would you go?"

poll_active = True

while poll_active:
    name = input("What's ur name?")
    place = input("Hello " + name.title() + ". " + hint)
    print(name.title() + " will visit " + place.title())
    
    current_state = input("Would u like polling to someone others?(yes/no)")
    if current_state == "no":
        poll_active = False
        print("Bye!")
    
    
