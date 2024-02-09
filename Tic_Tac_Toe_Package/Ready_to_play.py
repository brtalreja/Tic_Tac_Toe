def ready_to_play():
    
    choice = ''
    acceptable_values = ['Yes','No']
    
    while choice.isalpha() == False or choice not in acceptable_values:
        
        choice = input('Are you ready to play? Enter Yes or No: ')
        
        if choice.isalpha() == False:
            print('Sorry, this is not a valid input!')
        elif choice not in acceptable_values:
            print('Sorry, the only options are "Yes" or "No"!')
        else:
            if choice == acceptable_values[0]:
                return True
            elif choice == acceptable_values[1]:
                return False
            else:
                pass