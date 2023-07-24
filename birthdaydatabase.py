birthdays = {}

while True:
    print("hi, please enter a name for the birthday database or to search them up! OR ENTER TO QUIT, or 'birth' for all birthdays, or 'names' for all names")
    name = input()
    if name == "":
        break
    if name in birthdays:
        print(name + "'s birthday is: " + birthdays[name])
    elif name == "birth":
        for i in birthdays.values():
            print(i)
    elif name == "names":
        for i in birthdays.keys():
            print(i)
    else: 
        print(name + " is the first of their kind in the birthday database. What's their birthday?")
        birth = input()
        birthdays[name] = birth
        print("database updated!")