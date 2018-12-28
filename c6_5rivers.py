rivers = {
        "huanghe river":"china",
        "nile":"egypt",
        "henghe":"india"
        }
for river,country in rivers.items():
    print("The " + river.title() + " runs through " + country.title())

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
    
