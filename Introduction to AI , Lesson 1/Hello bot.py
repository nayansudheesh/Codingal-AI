print("hello , i am an AI bot")

name = input("enter your name")

print(f"nice to meet you {name}")
mood = input("how are you feeling?").lower()

if mood == "good":
    print(f"that is great to know {name}!")
elif mood == "bad":
    print(f"oh , hopefully you get better soon {name}")
else:
    print(f"i do not understand {name}")