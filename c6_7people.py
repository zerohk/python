person_1 = {
    "first_name":"tom",
    "last_name":"jerry",
    "city":"changsha",
    "age":22
    }

person_2 = {
    "first_name":"s",
    "last_name":"zc",
    "city":"changsha",
    "age":21
    }
    
person_3 = {
    "first_name":"jack",
    "last_name":"mary",
    "city":"changsha",
    "age":23
    }
    
people = [person_1,person_2,person_3]

for person in people:
    full_name = person["first_name"].title() + " " + person["last_name"].title()
    print("My name is " + full_name + ", i am " + str(person["age"]) + " years old," + " and i'm live in " + person["city"].title())
