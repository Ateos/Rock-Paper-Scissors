import random


hands = ['rock', 'paper', 'scissors']


def decision():

    opponent_choice = random.choice(hands)

    

    player_choice = raw_input("Please make your choice : ")
    print (' ')
    
    player_choice = player_choice.lower()

    
    if player_choice == 'rock' and opponent_choice == 'scissors':
        print ('Opponent chose scissors.')
        print (' ')
        print ('You Win!')
    elif player_choice == 'paper' and opponent_choice == 'rock':
        print ('Opponent chose rock.')
        print (' ')
        print ('You Win!')
    elif player_choice == 'scissors' and opponent_choice == 'paper':
        print ('Opponent chose paper.')
        print (' ')
        print ('You Win!')
    elif player_choice == opponent_choice:
        print ('Opponent chose ' + opponent_choice)
        print (' ')
        print ('It\'s a draw!')
    else:
        print ('Opponent chose ' + opponent_choice)
        print (' ')
        print ('You Lose!')

    print (' ')
    again = raw_input('Would you like to play again?  ')
    print (' ')
    if again == 'y' or 'yes':
        decision()
    else:
        print ('Thanks for playing!')
        raw_input()

    
decision()


