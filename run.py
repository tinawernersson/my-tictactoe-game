# My PP3 project at Code Institute 2024

def start_game():
    """
    Information on how to play, and the player can choose if they want to play against
    the computer or a friend.
    """
    print("Welcome to my Tic Tac Toe Game!\n")
    print("How to play:\nTic Tac Toe is a simple 2 player game where player 1 and player 2 take turns\nmarking a square in a 3*3 grid at a time using X and O.\nThe first player that marks its represented X or O with three marks\nin a vertical, horizontal or vertical row, wins.")
        
    execute_game = input("Press Enter To Start Game!")

  
  
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

    return (player_1, player_2)


def game_board():
    #not finished
    """
    Creates a new, blank gameboard
    """
    board = [["", "", ""],
            ["", "", ""],
            ["", "", ""]]        
    return board

def turns(player, count):
    """
    This function decides wich players turn it is
    """
    count = [0]
    while True:
        count += 1
        if player == player_1:
            print("Your turn player 1")
        elif player == player_2:
            print("Your turn player 2")
        break
   




start_game()
two_players()
game_board()
