"""PS 31 - Text-Based Adventure Game
Concepts: Conditions, Loops, Functions, Random
"""
import random

# ---- Settings (change these to run the test cases) ----
START_HEALTH = 100
FIXED_DAMAGE = None   # set to 30 for testing; None = random 10-40

# ---- Game state ----
health = START_HEALTH
score = 0


def get_damage():
    """Return monster damage: fixed for testing, otherwise random 10-40."""
    if FIXED_DAMAGE is not None:
        return FIXED_DAMAGE
    return random.randint(10, 40)


def forest():
    """Starting place: show the menu and return a valid choice."""
    print("\nYou are in the Forest.")
    print("1. Cave  2. River  3. Quit")
    choice = input("Enter your choice: ").strip()
    if choice in ("1", "2", "3"):
        return choice
    print("Invalid choice. Enter 1, 2 or 3.")
    return None


def cave():
    """Monster attacks; if the player survives, they find a key."""
    global health, score
    damage = get_damage()
    health -= damage
    if health < 0:
        health = 0
    print(f"Cave: Monster attacks! Damage: {damage}. Health: {health}")
    if health > 0:
        score += 20
        print(f"You found a key! Score: {score}")


def river():
    """Treasure gives +50 score."""
    global score
    score += 50
    print(f"River: You found a treasure! Score: {score} | Health: {health}")


def main():
    while health > 0:
        choice = forest()
        if choice is None:        # invalid input: no health lost
            continue
        if choice == "1":
            cave()
        elif choice == "2":
            river()
        else:
            print(f"You left the adventure. Final score: {score} | Health: {health}")
            return
    print(f"Game Over! Final score: {score}")


if __name__ == "__main__":
    main()