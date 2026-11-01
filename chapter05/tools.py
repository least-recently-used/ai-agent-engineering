import datetime
import secrets
import random
from pathlib import Path

# The data folder next to this file, so it works no matter where you run Python from
DATA_DIR = Path(__file__).parent / "data"

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def roll_dice(sides=6):
    """Roll a dice with the specified number of sides."""
    return random.randint(1, sides)


def generate_password(length=8):
    """Generate a random string of specified length."""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def open_file(file_name):
    """Read a file from the data folder and return its contents."""
    file_path = (DATA_DIR / file_name.strip()).resolve()

    # Only allow files inside the data folder (blocks things like "../.env")
    if not file_path.is_relative_to(DATA_DIR.resolve()):
        return f"Error: '{file_name}' is outside the data folder."

    try:
        return file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return f"Error: The file '{file_name}' was not found in the data folder."
    except IsADirectoryError:
        return f"Error: '{file_name}' is a folder, not a file."