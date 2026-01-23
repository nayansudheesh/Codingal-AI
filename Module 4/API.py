import requests



def get_random():
    #getting a random joke from the Joke API
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Full JSON response: {response.json()}")

        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']} "
    else:
        return "failed to retreive joke"

def main():

    print("welcome to the random joke genarator")
    while True:
        user_input = input("Press to enter to get a new joke , or type q to exit").strip().lower()

        if user_input in "q":
            print("goodbye")
            break
    joke = get_random()
    print(joke)

if __name__ == "__main__":
    main()
