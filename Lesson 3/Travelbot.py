import re , random
from colorama import Fore , init

init(autoreset=True)

destination = {
    "beaches" : ["Bali , Maldives , Phuket"],
    "Mountains": ["Swiss alps" , "Himalayas" , "Rocky Mountains"],
    "Cities": ["New Delhi" , "Travancore" , "Trivandrum"]

}

jokes = [
    "why didnt the programmer go to the forest? Too many bugs!",
    "Why did the computer go to the doctor? it had a virus!",
    "why do travelers feel hot? because of their hot spots!",
]

def normalize_input(text):
    return re.sub(r"\s+", "" , text.strip().lower())

def recommend():
    print(Fore.CYAN  + "Travelbot: Beaches , Mountains , or cities?")
    preference = input("You:")
    preference = normalize_input(preference)

    if preference in destination:
        suggestion = random.choice(destination[preference])
        print(f"Travelbot: How about {suggestion}?")
        print(f"Do you like it? {Fore.GREEN}Y / {Fore.RED} N")
        answer = input("You:").lower()

        if answer == "y" or answer == "yes":
            print(f"Awesome! enjoy your stay at {suggestion}")
        elif answer == "n" or answer =="no":
            print("lets try again")
            recommend()
        else:
            print(f"{Fore.RED} Sorry , I do not have that destination")

        show_help()

def packing_tips():
    print("Travelbot: Where to?")
    location = normalize_input(input("You:"))
    print("Travelbot: How many days?")
    days = normalize_input(input("You:"))

    print(f"Packing trips for {days} in {location}")
    print("-Wear Versatile clothing , always have backup clothes")
    print("-Bring chargers and adapters for your electronic devices")
    print(f"-check the weather forcast for the next {days} days")


def tell_joke():
    print(Fore.CYAN + random.choice(jokes))

def show_help():
    print("I can:")
    print("-Tell Jokes,(say jokes)")
    print("-Offer you packing tips,(say packing)")
    print("Suggest travel spots.(say recomendation)")
    print("type exit or bye to exit the program")

def chat():
    print("Hello! im travelbot!")
    name = input("Your name?")
    print("nice to meet you " , name)

    show_help()

    while True:
        user_input = input(f"{Fore.LIGHTBLUE_EX}  {name}:" )
        user_input = normalize_input(user_input)

        if "reccomend" in user_input:
            recommend()
        elif "packing" in user_input:
            packing_tips()
        elif "joke" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input:
            print("Travelbot: Goodbye!")
            break
        else:
            print("could you rephrase?")
            show_help()

if __name__ == "__main__":
    chat()