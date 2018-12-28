favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +language.title() + ".")

joint = ["jen","sarah"]

for user in favorite_languages.keys():
    if user in joint:
        print("Thanks join us," + user.title())
    else:
        print("You can join us now," + user.title())
