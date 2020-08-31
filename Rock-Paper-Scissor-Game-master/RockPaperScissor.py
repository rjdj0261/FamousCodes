import random
import time
print('You can write \'rock\', \'paper\' or \'scissor\' \nor write like \'r\', \'p\', \'s\'\nfor rock, paper, scissor respectively.')
print('Also You can write 1 for rock and 2 for paper and\n3 for scissor.')
print('Write Exit/Close to close the program')
time.sleep(3)
def game():
    computer_choice_list = 'rock', 'paper', 'scissor'
    rocklist = 'rock', 'r', '1', '1st one', 'first one', '1st', 'first', '👊'
    paperlist = 'paper', 'p', '2', '2nd one', 'second one', '2nd', 'second', '✋'
    scissorlist = 'scissor', 's', '3', '3rd one', 'third one', '3rd', 'third', 'last one', 'last', '✌'
    get_out = 'exit', 'quit', 'back', 'off', 'get out', 'out', 'close', 'turn off', 'e', 'q', 'o', 'c'
    print('\nChoose any of these.\nRock/paper/scissor.')
    user_choice = input('=> ')
    computer_choice = random.choice(computer_choice_list)
    if user_choice.lower() in rocklist and computer_choice == 'rock':
        print('\nComputer = rock 👊 \nYou = rock 👊.')
        print('--Match tied--')
        time.sleep(3)
        game()
    elif user_choice.lower() in paperlist and computer_choice == 'paper':
        print('\nComputer = paper ✋ \nYou = paper ✋')
        print('--Match tied--')
        time.sleep(3)
        game()
    elif user_choice.lower() in scissorlist and computer_choice == 'scissor':
        print('\nComputer = scissor ✌ \nYou = scissor ✌')
        print('--Match tied--')
        time.sleep(3)
        game()
    elif user_choice.lower() in rocklist and computer_choice == 'scissor':
        print('\nComputer = scissor ✌ \nYou = rock 👊 ')
        print('--Congratulations! You win--')
        time.sleep(3)
        game()
    elif user_choice.lower() in paperlist and computer_choice == 'rock':
        print('\nComputer = rock 👊 \nYou = paper ✋')
        print('--Congratulations! You win--')
        time.sleep(3)
        game()
    elif user_choice.lower() in scissorlist and computer_choice == 'paper':
        print('\nComputer = paper ✋ \nYou = scissor ✌')
        print('--Congratulations! You win--')
        time.sleep(3)
        game()
    elif user_choice.lower() in rocklist and computer_choice == 'paper':
        print('\nComputer = paper ✋ \nYou = rock 👊 ')
        print('--You lose--')
        time.sleep(3)
        game()
    elif user_choice.lower() in paperlist and computer_choice == 'scissor':
        print('\nComputer = scissor ✌ \nYou = paper ✋ ')
        print('--You lose--')
        time.sleep(3)
        game()
    elif user_choice.lower() in scissorlist and computer_choice == 'rock':
        print('\nComputer = rock 👊 \nYou = scissor ✌')
        print('--You lose--')
        time.sleep(3)
        game()
    elif user_choice.lower() in get_out:
        print('Program closed')
        print("Don't forget to star. 😋")
        exit()
    else:
        print('invalid input')
        time.sleep(1)
        game()
game()
