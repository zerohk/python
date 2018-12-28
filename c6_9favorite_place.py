favorite_place = {
                "tom":["beijing","shanghai"],
                "jerry":["tianjin","hefei"],
                "marry":["guangzhou","shenzhen"]
                }
for people,places in favorite_place.items():
    print(people.title() + " loves these cities:")
    for place in places:
        print(place.title())
    print("\n")
    
     
