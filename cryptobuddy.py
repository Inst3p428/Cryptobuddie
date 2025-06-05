# ========== Personality & Voice ==========
def get_greeting():
    greetings = [
        "Hey there, crypto crusader! Ready to ride the blockchain wave?",
        "Yo! Looking to make green gains and save the planet? Let’s dive in. 🌍📈",
        "Welcome back, digital investor! Let’s find your next coin crush. 💰",
        "Sup champ! Wanna know which coin is mooning *and* eco-friendly? I got you.✨",
    ]
    return random.choice(greetings)

def speak(message):
    print(f"Cryptobudie 🤖: {message}")

#----sample crypto_bd
crypto_db = {
    "EcoCoin": {
        "price": 2.5,
        "sustainability_score": 9,
        "growth_rate": 7,
        "market_cap": 500000000,
        "launch_year": 2017
    },
    "BitSmart": {
        "price": 50.0,
        "sustainability_score": 5,
        "growth_rate": 8,
        "market_cap": 1000000000,
        "launch_year": 2015
    },
    "GreenToken": {
        "price": 3.0,
        "sustainability_score": 10,
        "growth_rate": 6,
        "market_cap": 200000000,
        "launch_year": 2018
    }
}

#----Rule-based answers using if statements.
disclaimer = "⚠ Crypto is risky — always do your own research!"

import random

def chatbot():
    greet()

while True: 
    user_query = input("\nYou: ").lower()
    
    if "exit" in user_query or "bye" in user_query:
        print("CryptoBuddy: Catch you later! 💰 Stay smart.")
        break

    elif "sustainable" in user_query:
        coin = get_most_sustainable()
        print(f"CryptoBuddy: 🌱 {coin} is the most sustainable option with minimal energy use!")
        print(disclaimer)

    elif "trending" in user_query or "rising" in user_query:
        coins = get_trending_up()
        print(f"CryptoBuddy: 📈 These coins are trending up: {', '.join(coins)}")
        print(disclaimer)

    elif "profitable" in user_query or "best to invest" in user_query or "long-term" in user_query:
        coin = get_most_profitable()
        if coin != "None":
            print(f"CryptoBuddy: 💸 For long-term growth, {coin} looks profitable with a rising trend and high market cap!")
        else:
            print("CryptoBuddy: Hmm, no highly profitable coins found at the moment.")
        print(disclaimer)

    elif "info" in user_query or "details" in user_query:
        print("\nCryptoBuddy: 📊 Here are the details of all coins in the database:")
        for name, stats in crypto_db.items():
            print(f"\n{name}:")
            for key, value in stats.items():
                print(f"  {key}: {value}")

    elif "cheap" in user_query or "low price" in user_query:
        coin = min(crypto_db, key=lambda x: crypto_db[x]["price"])
        price = crypto_db[coin]["price"]
        print(f"CryptoBuddy: 🪙 {coin} is the cheapest coin right now at ${price:.2f}. Great for beginners!")
        print(disclaimer)

    elif "fastest" in user_query or "quick" in user_query:
        coin = max(crypto_db, key=lambda x: crypto_db[x]["growth_rate"])
        rate = crypto_db[coin]["growth_rate"]
        print(f"CryptoBuddy: 🚀 {coin} is the fastest growing coin with a growth rate of {rate}%!")
        print(disclaimer)

    elif "oldest" in user_query or "history" in user_query:
        coin = min(crypto_db, key=lambda x: crypto_db[x]["launch_year"])
        year = crypto_db[coin]["launch_year"]
        print(f"CryptoBuddy: 📜 {coin} is the oldest coin — launched in {year}!")
        print(disclaimer)

    elif "random" in user_query or "surprise" in user_query:
        coin = random.choice(list(crypto_db.keys()))
        print(f"CryptoBuddy: 🎲 Just for fun... check out {coin}! Might be your lucky pick today.")
        print(disclaimer)

    else:
        print("CryptoBuddy: 🤖 Sorry, I didn’t get that. Try asking about trending, cheap, fastest-growing, oldest, or even a random coin!")

chatbot()


