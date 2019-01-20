sandwich_orders = ["pure","chicken","beef","vege","egg"]
finished_sandwich = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I made ur " + current_order + " sandwich\n")
    finished_sandwich.append(current_order)

for sandwich in finished_sandwich:
    print(sandwich)
        
