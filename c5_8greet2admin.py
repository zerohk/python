users = ["admin","jack","rose","tom","jerry"]
for user in users:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello," + user.title() + " thank you for logging in again")
