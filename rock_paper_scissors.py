import random
from enum import Enum, auto

class Move(Enum):
    """
    Represents possible moves in the game.
    Can be extended with new moves like Lizard, Spock, etc.
    """
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

# Mapping from single-letter inputs to Move enums
INPUT_MAP = {
    'r': Move.ROCK,
    'p': Move.PAPER,
    's': Move.SCISSORS
}

def parse_player_move(user_input: str) -> Move:
    """
    Converts a user string (e.g., 'r', 'p', 's') into the corresponding Move Enum.
    Raises an exception if invalid.
    """
    user_input = user_input.lower().strip()
    if user_input in INPUT_MAP:
        return INPUT_MAP[user_input]
    else:
        raise ValueError(f"Invalid input '{user_input}'. Expected one of {list(INPUT_MAP.keys())}.")

def get_computer_move() -> Move:
    """
    Randomly picks one of the possible moves for the computer.
    This can be expanded to incorporate AI or weighting logic.
    """
    return random.choice(list(Move))

def determine_winner(player_move: Move, computer_move: Move) -> str:
    """
    Determines the outcome of a single round given the player's move and the computer's move.
    Returns "win", "lose", or "draw".
    """
    # Winning logic: if you add new moves (e.g., Lizard, Spock), expand conditions here
    if player_move == computer_move:
        return "draw"

    winning_combos = {
        (Move.ROCK,     Move.SCISSORS),
        (Move.PAPER,    Move.ROCK),
        (Move.SCISSORS, Move.PAPER)
    }

    if (player_move, computer_move) in winning_combos:
        return "win"
    else:
        return "lose"

def play_round(player_input: str) -> bool:
    """
    Plays a single round of RPS. 
    - Converts the player's input string into a Move.
    - Gets a random Move for the computer.
    - Prints the outcome.
    Returns True if the user should continue playing, False to stop.
    """
    try:
        player_move = parse_player_move(player_input)
    except ValueError as e:
        print(e)
        return True  # Let them try again

    computer_move = get_computer_move()
    print(f"The computer chose {computer_move.name.title()}.")

    result = determine_winner(player_move, computer_move)
    if result == "win":
        print("You win!")
    elif result == "draw":
        print("It's a draw!")
    else:
        print("You lose!")

    # Prompt for next action
    choice = input("Type 'n' to quit or 'r', 'p', 's' to keep playing: ").strip().lower()
    if choice == 'n':
        return False
    else:
        # They want to keep playing, so we recursively play the next round
        return play_round(choice)

def main():
    """
    The main entry point for the Rock-Paper-Scissors game.
    Contains optional expansions like a scoreboard or multiple-round logic.
    """
    # Future expansions: scoreboard, multi-round setups, a match winner, etc.
    print("Welcome to Rock-Paper-Scissors!")
    user_input = input("Enter r for rock, p for paper, or s for scissors: ").lower().strip()
    keep_playing = True

    while keep_playing:
        keep_playing = play_round(user_input)
        if keep_playing:
            # Prepare for next loop iteration; user_input is set inside `play_round`.
            user_input = ""  # We'll rely on the user input from inside play_round
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
