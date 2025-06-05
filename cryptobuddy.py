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
