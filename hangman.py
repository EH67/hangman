#TODO can also add a time module into this
import random

word1 = random.choice(open("words").readlines()).strip()
user = ''
j = 0
guess = [*('_' * len(word1.strip()))]
list = [*'abcdefghijklmnopqrstuvwxyz']
gstring = ''.join(guess)
already_guessed=''
print ('Current Guess: {}'.format(gstring))

while j != 9 or gstring != word1:
    user=input('Enter your guess: ').strip().lower()
    for i in range(len(word1)):
        if user == word1[i]:
            guess[i] = user
    if user not in guess:
        j += 1
    gstring = ''.join(guess)
    print('\nCurrent Guess: {}'.format(gstring))
    list.remove(user)
    slist = ' '.join(list)
    print('You have used up {} out of 9 wrong guesses. You can still guess these letters: {}'.format(j, slist))

    if j == 9:
        print ("Aw you've run out of guesses. Try again next time! The answer is " + word1)
        break
    elif gstring == word1:
        print("You won!")
        break
    else:
        pass



