# My PP3 project at Code Institute 2024

def intro():
    """
    Information on how to play, and the player can choose if they want to play against
    the computer or a friend.
    """
    print("Welcome to my Tic Tac Toe Game!\n")
    print("How to play:\nTic Tac Toe is a simple 2 player game where player 1 and player 2 take turns\nmarking a square in a 3*3 grid at a time using X and O.\nThe first player that marks its represented X or O with three marks\nin a vertical, horizontal or vertical row, wins.")

    print("\nDo you want to play with a friend or against the computer?\nType 'F' for friend or 'C' for computer. Press Enter to start game.")
    print(input("Start Game:"))


def start_game():
    """
    Starts the game depending on wich choice the player has made
    """
    if one_player == "C":
        print("You decided to play against the computer.")
    else:
        two_players = "F"
        print("You decided to play with a friend.")  
             

def two_players():
# This function decides the players' symbols
    player_1 = input("Player 1, do you want to be X or O? ")
    if player_1 == "X":
        player_2 = "O"
        print("Player 2, you are O. ")
    else:
        player_2 = "X"
        print("Player 2, you are X. ")
    input("Press enter to continue.")
    print("\n")
    #return (player_1, player_2)
    print(player_1, player_2)

def one_player():
    """
    This function executes if the player wants to play against the computer
    """
    player_1 = input("Player 1, do you want to be X or O? ")
    if player_1 == "X":
        computer = "O"
        print("You are X and computer is O.")
    else:
        computer = "X"
        print("You are O and computer is X. ")
    #return (player_1, computer)
    print(player_1, computer)

def game_board():
    """
    Creates a new, blank gameboard
    """
    board = [["", "", ""],
            ["", "", ""],
            ["", "", ""]]        
    print(board)
    #return board


intro()
start_game()
one_player()
two_players()
game_board()
