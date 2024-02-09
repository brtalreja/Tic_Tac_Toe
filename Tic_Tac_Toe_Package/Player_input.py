def player_input():
    
    choice = ''
    acceptable_values = ['X','O']
    
    while choice.isalpha() == False or choice not in acceptable_values:
        
        choice = input('Player 1: Do you want to be X or O? ')
        
        if choice.isalpha() == False:
            print('Sorry, this is not a valid input!')
        elif choice not in acceptable_values:
            print('Sorry, the only options are "X" or "O"!')
        else:
            if choice == 'X':
                return ('X','O')
            else:
                return ('O','X')