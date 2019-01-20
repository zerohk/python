favo_num = {
    "tom":[22,3,4,23,45],
    "jerry":[46,7,8,21],
    "jack":[20,53,32,99,520,666],
    "rose":[45]
    }

for person,numbers in favo_num.items():
    if len(numbers) == 1:
        print(person.title() + "'s favorite number is:")
        for number in numbers:
            print(number)
    else:
        print(person.title() + "'s favorite numbers are:")
        for number in numbers:
            print(number)
    print("\n")
