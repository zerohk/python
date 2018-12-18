guest = ["Tom","Jerry","Mary"]
message = "I want to invite you to my dinner,"
print(message + guest[0] + "\n")
print(message + guest[1] + "\n")
print(message + guest[2] + "\n")

#3_5
absent = guest.pop(1)
print("I am sorry but " + absent + " cant go to our dinner\n")
guest.insert(1,'Lily')
print(message + guest[0] + "\n")
print(message + guest[1] + "\n")
print(message + guest[2] + "\n")

#3_6
print("I bought a bigger table\n")
guest.insert(0,'Jack')
guest.insert(2,'Rose')
guest.append('Washinton')
print(message + guest[0] + "\n")
print(message + guest[1] + "\n")
print(message + guest[2] + "\n")
print(message + guest[3] + "\n")
print(message + guest[4] + "\n")
print(message + guest[5] + "\n")

#3_7
print("I can only invite 2 pepole")
pop1 = guest.pop()
pop2 = guest.pop()
print(len(guest))
pop3 = guest.pop()
pop4 = guest.pop()
message = "Sorry,"
print(message + pop1)
print(message + pop2)
print(message + pop3)
print(message + pop4)

message = "You are still here,"
print(message + guest[0])
print(message + guest[1])

del guest[1]
del guest[0]

print(guest)




