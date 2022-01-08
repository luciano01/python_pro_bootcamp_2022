print('Welcome to Tresure Island.')
print('Your mission is to find the treasure.')

choice1 = input(
    'You\'re at a crossroad, where do you want to go? Type "Left" or "Right". ').lower()


if(choice1 == 'left'):
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if(choice2 == 'wait'):
        choice3 = input(
            'You arrive at the island unharmed. There is a house with 3 doors. On red, on yellow and one blue. Which colour do you choose? ')
        if(choice3 == 'Red'):
            print('It\'s a room full of fire. Game Over.')
        elif(choice3 == 'Yellow'):
            print('You found the treasure. You Win!')
        elif(choice3 == 'Blue'):
            print('You enter a room of beasts. Game Over.')
        else:
            print('You chose a door that doesn\'t exist. Game Over.')
    else:
        print('You got attacked by an angry trout. Game Over.')
else:
    print('You fell into a hole. Game Over.')
