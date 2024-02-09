from Tic_Tac_Toe_Package import Choose_first
from Tic_Tac_Toe_Package import Display_board
from Tic_Tac_Toe_Package import Full_board_check
from Tic_Tac_Toe_Package import Place_marker
from Tic_Tac_Toe_Package import Player_choice
from Tic_Tac_Toe_Package import Player_input
from Tic_Tac_Toe_Package import Ready_to_play
from Tic_Tac_Toe_Package import Replay
from Tic_Tac_Toe_Package import Space_check
from Tic_Tac_Toe_Package import Win_check

print('Welcome to Pythonic Tic-Tac-Toe')

while True:
    board = [' '] * 10

    player1_marker, player2_marker = Player_input.player_input()

    turn = Choose_first.choose_first()
    print(turn + ' will go first')

    game_on = Ready_to_play.ready_to_play()

    while game_on:
        if turn == 'Player 1':
            
            Display_board.display_board(board)
            position = Player_choice.player_choice(board)
            Place_marker.place_marker(board,player1_marker,position)
            
            if Win_check.win_check(board,player1_marker):
                Display_board.display_board(board)
                print("Congratulations " + turn + "! You have won the game!")
                game_on=False
            else:
                if Full_board_check.full_board_check(board):
                    Display_board.display_board(board)
                    print("Oops! This is a tie")
                    game_on=False
                    break
                else:
                    turn = 'Player 2'
                    
        else:
            
            Display_board.display_board(board)
            position = Player_choice.player_choice(board)
            Place_marker.place_marker(board,player2_marker,position)
            
            if Win_check.win_check(board,player2_marker):
                Display_board.display_board(board)
                print("Congratulations " + turn + "! You have won the game!")
                game_on=False
            else:
                if Full_board_check.full_board_check(board):
                    Display_board.display_board(board)
                    print("Oops! This is a tie")
                    game_on=False
                    break
                else:
                    turn = 'Player 1'
                
    if not Replay.replay():
        break