import random

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
player_move = input('Enter r for rock, p for paper, or s for scissors: ')

done = False

while not done:
    if player_move == 'r':
        player_move = ROCK
    elif player_move == 'p':
        player_move = PAPER
    elif player_move == 's':
        player_move = SCISSORS
    else:
        raise SystemExit('Invalid Input. Try again...')

    computer_move = ''
    if random.randint(1, 3) == 1:
        computer_move = ROCK
    elif random.randint(1,3) == 2:
        computer_move = PAPER
    else:
        computer_move = SCISSORS
    print(f"The computer chose {computer_move}.")

    if (player_move == ROCK and computer_move == SCISSORS) or \
            (player_move == PAPER and computer_move == ROCK) or \
            (player_move == SCISSORS and computer_move == PAPER):
        print("You win!")
    elif player_move ==computer_move:
        print("Draw!")
    else:
        print("You lose!")

    play_again = input('Type n to quit or r, p, s to play again: ')
    if play_again == 'n':
        done = True
    else:
        player_move = play_again
if done:
    print('Thank you for playing')