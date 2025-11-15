
print("hello! this is the Hello Chatbot , please enter your name")
name = input()
mood = input("how  do you feel?").lower()
if mood == ("okay") or mood == ("fine"):
        print("good to know ")
elif mood == "great" or mood =="good":
        print("thats great!")
elif mood == "sad" or mood == "bad":
        print("hopefully you get better soon and whatever is making you feel bad goes away")
else:
        print("i do not understand , please try again")
