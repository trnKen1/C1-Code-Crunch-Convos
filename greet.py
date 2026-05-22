"""greet.py — greet the user by name."""


def greet(name: str) -> str:
    """Return a friendly greeting for ``name``."""
    return f"Hello, {name}! Welcome to Code Crunch Convos."


if __name__ == "__main__":
    user_name: str = input("What is your name? ")
    print(greet(user_name))