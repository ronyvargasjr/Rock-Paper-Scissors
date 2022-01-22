import random

def game():
    user = input("Rock (r), Paper (p), Scissor (s)").lower()
    computer = random.choice (["r", "p", "s"])
    print(f"User chose: {user}")
    print(f"Computer chose: {computer}")
    while user:
        if match(user,computer):
            return "You won!!"
        elif match(computer,user):
            return "You lost."
        elif user == computer:
            print("Tie!")
            return game()
        else:
            print("Invalid. Try again. Use 'r', 'p', or 's'.")
            return game()


def match(player,opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
        or (player == "p" and opponent == "r"):
        return True

print(game())
