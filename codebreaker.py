import random

def generate_secret_code():
    """Generiere einen zufälligen Geheimcode."""
    return [random.randint(0, 9) for _ in range(4)]

def get_user_guess():
    """Lese die Benutzereingabe für einen Ratenversuch ein."""
    try:
        guess = [int(x) for x in input("Gib deinen 4-stelligen Rat ein (0-9 getrennt durch Leerzeichen): ").split()]
        if len(guess) != 4 or any(num < 0 or num > 9 for num in guess):
            raise ValueError("Ungültige Eingabe. Bitte gib genau vier Zahlen von 0 bis 9 ein.")
        return guess
    except ValueError as e:
        print(f"Fehler: {e}")
        return get_user_guess()

def evaluate_guess(secret_code, user_guess):
    """Bewerte den Ratenversuch des Benutzers."""
    correct_position = sum(1 for x, y in zip(secret_code, user_guess) if x == y)
    correct_digits = sum(min(secret_code.count(digit), user_guess.count(digit)) for digit in set(user_guess)) - correct_position
    return correct_position, correct_digits

def play_game():
    """Hauptfunktion für das Spiel."""
    secret_code = generate_secret_code()
    attempts = 0

    print("Willkommen bei Number Code Breaker!")
    print("Errate den 4-stelligen Code mit Zahlen von 0 bis 9.")

    while True:
        user_guess = get_user_guess()
        attempts += 1

        correct_position, correct_digits = evaluate_guess(secret_code, user_guess)

        print(f"Ergebnis: {correct_position} an der richtigen Position, {correct_digits} an der falschen Position.")

        if correct_position == 4:
            print(f"Herzlichen Glückwunsch! Du hast den Code in {attempts} Versuchen geknackt.")
            break

if __name__ == "__main__":
    play_game()
