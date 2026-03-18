import random


def generate_secret_number(low=1, high=100):
    return random.randint(low, high)


def parse_guess(raw_value):
    try:
        return int(raw_value.strip())
    except (ValueError, AttributeError):
        return None


def check_guess(guess, secret_number):
    if guess < secret_number:
        return "Too Low"
    if guess > secret_number:
        return "Too High"
    return "Correct"


def calculate_score(attempts, starting_score=100, penalty=10):
    return max(0, starting_score - (attempts * penalty))


def reset_game():
    return {
        "secret_number": generate_secret_number(),
        "attempts": 0,
        "score": 100,
        "game_over": False,
        "history": [],
    }