import random

print('------------------------')
print('      guess number ')
print('------------------------')

target_number = random.randint(0, 100)
user_guess_number = None

user_name = input('whats your name? ')

while user_guess_number != target_number:
    user_guess = input('guess a number between 1 - 100 ')

    user_guess_number = int(user_guess)

    if user_guess_number < target_number:
        # string formatting used to convert different values to string
        print('sorry {1}, your guess of {0} is too low'.format(user_guess_number, user_name))
    elif user_guess_number > target_number:
        # dont need to specify location if order is the same
        print('sorry {}, your guess of {} is too low'.format(user_name, user_guess_number))
    else:
        print('correct!')
