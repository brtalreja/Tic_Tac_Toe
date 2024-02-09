from Tic_Tac_Toe_Package import Display_board
from Tic_Tac_Toe_Package import Space_check

def player_choice(board):
    choice = 'wrong'
    acceptable_values = list(range(1,10))
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
        
        choice = input('Choose your next position: (1-9) ')
        
        if choice.isdigit() == False:
            print('Sorry, this is not a valid input!')
        elif int(choice) not in acceptable_values:
            Within_range = False
            print('Sorry, the only options are 1 to 9!')
        else:
            Within_range = True
            if Space_check.space_check(board,int(choice)):
                return int(choice)
            else:
                Display_board.display_board(board)
                print('This position is already filled. Please select any other unfilled position!')