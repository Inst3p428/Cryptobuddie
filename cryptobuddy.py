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


