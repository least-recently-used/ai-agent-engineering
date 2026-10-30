import datetime
import secrets
import random

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def roll_dice(sides=6):
    """Roll a dice with the specified number of sides."""
    return random.randint(1, sides)


def generate_password(length=8):
    """Generate a random string of specified length."""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(secrets.choice(alphabet) for _ in range(length))


