current_users = ["tom","jerry","jack","rose","mac"]
new_users = ["jack","Marry","Tom","Leo","mic"]

for user in new_users:
    if user.lower() in current_users:
        print("You need change the name")
    else:
        print("This username is not used")
