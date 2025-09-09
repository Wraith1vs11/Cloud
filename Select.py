import requests
import os
import sys
from colorama import init, Fore, Style

os.system("clear")
init(autoreset=True)

while True:
    print(Fore.LIGHTWHITE_EX + "1. " + Fore.YELLOW + Style.BRIGHT + "Delta Executor")
    print(Fore.LIGHTWHITE_EX + "2. " + Fore.YELLOW + Style.BRIGHT + "Arceus X NEO Executor")
    print(Fore.LIGHTWHITE_EX + "3. " + Fore.YELLOW + Style.BRIGHT + "Krnl Executor")
    print(Fore.LIGHTWHITE_EX + "4. " + Fore.LIGHTRED_EX + Style.BRIGHT + "Exit")

    choice = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "🚗 Please Select Your Tool: " + Style.RESET_ALL).strip()

    if choice == "1":
        url = "https://raw.githubusercontent.com/Wraith1vs11/Cloud/refs/heads/main/Delta.py"
    elif choice == "2":
        url = "https://raw.githubusercontent.com/Wraith1vs11/Cloud/refs/heads/main/Arceus.py"
    elif choice == "3":
        url = "https://raw.githubusercontent.com/Wraith1vs11/Cloud/refs/heads/main/Krnl.py"
    elif choice == "4":
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "👋 Exiting...")
        sys.exit(0)
    else:
        print(Fore.LIGHTRED_EX + "🥩 Invalid Choice, Please Try Again! 🍖")
        continue

    try:
        print(Fore.LIGHTBLACK_EX + "⏳ " + Fore.LIGHTYELLOW_EX + "Downloading & Executing... Please wait.")
        response = requests.get(url)
        response.raise_for_status()
        exec(response.text)
    except Exception as e:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + f"🏎️ Error: {e} 🏍️")
