sandwich_orders = ["pastrami","pure","chicken","pastrami","beef","pastrami","egg"]
finished_sandwich = []
print("I am sorry ,pastrami is sold out!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I made ur " + current_order + " sandwich\n")
    finished_sandwich.append(current_order)

for sandwich in finished_sandwich:
    print(sandwich)
