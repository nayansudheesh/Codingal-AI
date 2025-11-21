from colorama import Fore,Style, init
from textblob import TextBlob

init(autoreset=True)

print(f"{Fore.CYAN} Welcome , fellow sentiment spy!{Style.RESET_ALL}!")

user_name = input("whats your name fellow agent?").strip()
if not user_name:
    user_name = "Mystery Agent"
print(f"Hello!, {Fore.RED}{user_name}{Style.RESET_ALL}")
conversation_history = []
print(f"{Fore.YELLOW} Instructions:{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}Type the following to get sentiment analysis{Style.RESET_ALL}")
print(f"1) Type {Fore.BLUE}history{Style.RESET_ALL} to get a history of your conversation with the AI")
print(f"2) Type  to clear conversation history")
print(f"3) type {Fore.RED}exit{Style.RESET_ALL}to leave the program{Style.RESET_ALL}")

while True:
    user_input = input("your input").strip()

    if not user_input:
        print("please enter an input")
    elif user_input.lower() == "exit":
        print(f"goodbye {Fore.LIGHTRED_EX}{user_name}{Style.RESET_ALL}")
    elif user_input.lower() == "reset":
        conversation_history = []
        print(f"{Fore.YELLOW}Conversation History has been reset{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print("no conversation yet")
        else:
            print("--- Conversation History --- ")
            for text , polarity , sentiment_type in conversation_history:
                color = ""
                emoji = ""
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Neutral":
                    color = Fore.WHITE
                    emoji = "😐"
                elif sentiment_type == "Negative":
                    color = Fore.BLACK
                    emoji = "😔"
                print(f"Text: {text} | Polarity: {color} {polarity:2f}{Style.RESET_ALL} | Sentiment: {color} {sentiment_type} {Style.RESET_ALL}  ")
            print("---------------------------------------------------------------------------------------")
        continue
    else:
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity
        sentiment_type = "Neutral"
        color = Fore.WHITE
        emoji = "😐"

        if polarity > 0.25:
            sentiment_type = "Positive"
            color = Fore.GREEN
            emoji = "😊"
        elif polarity < -0.25:
            sentiment_type = "Negative"
            color = Fore.BLACK
            emoji = "😔"

        
        conversation_history.append((user_input , polarity , sentiment_type))

        print(f"Sentiment: {color}{sentiment_type}{emoji}{Style.RESET_ALL} | Polarity: {color} {polarity:2f}{Style.RESET_ALL}")
        


