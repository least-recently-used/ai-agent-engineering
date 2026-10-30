import re

from tools import get_current_time, generate_password, roll_dice


def has_word(pattern, text):
    """Check if pattern appears as a whole word (so "time" doesn't match "sometimes")."""
    return re.search(rf"\b{pattern}\b", text) is not None


def execute_tool_command(command):
    """Execute a tool command and return the result."""
    text = command.lower()

    if has_word("time", text):
        return get_current_time()
    elif has_word("dice", text):
        sides = 20 if has_word("d?20", text) else 6  # matches "20" or "d20"
        return roll_dice(sides)
    elif has_word("passwords?", text):
        length = 10  # Default length
        return generate_password(length)
    else:
        return None  # No tool command found


