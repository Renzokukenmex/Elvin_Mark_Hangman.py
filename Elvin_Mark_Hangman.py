#importing docx package for access to word_list.docx
import docx


#Importing the choice method from the random module for random word selection.
from random import choice

#Defining the the document class object as 'file'
file = docx.Document('word_list.docx')

#introducing the random selection of text/word held within paragraphs within the word file.
word = choice([p.text for p in file.paragraphs])




#initial values for guessed/wrong defined

guessed = []

wrong = []


#Tracking attempts for limiting number of goes

attempts = 7



while attempts > 0:



    result = ''



#Guessing a letter of the word

    for letter in word:

        if letter in guessed:

            result = result + letter

        else:

            result = result + '*'



    if result == word:

        break



    print ('Please enter your next guess:', result)

    print (attempts, 'attempts left')



    guess = input()



# confirming if guess is correct, if not reducing guesses left.

    if guess in guessed or guess in wrong:

        print ('You\'ve already guessed this letter', guess)

    elif guess in word:

        print('Well done!, You guessed well')

        guessed.append(guess)

    else:

        print('Unlucky!, try again')

        attempts = attempts - 1

        wrong.append(guess)





# Hangman ASCII art linked to remaining goes (attempts)

    if attempts == 7:

        print ('__________')

        print ('|    |')

        print ('|')

        print ('|')

        print ('|')

        print ('|')

        print ('|_________')

        print ('')

    elif attempts == 6:

        print ('__________')

        print ('|    |')

        print ('|    O')

        print ('|')

        print ('|')

        print ('|')

        print ('|_________')

        print ('')

    elif attempts == 5:

        print ('__________')

        print ('|    |')

        print ('|    O')

        print ('|    |')

        print ('|')

        print ('|')

        print ('|_________')

        print ('')

    elif attempts == 4:

        print ('__________')

        print ('|    |')

        print ('|    O')

        print ('|    |')

        print ('|    |')

        print ('|')

        print ('|_________')

        print ('')

    elif attempts == 3:

        print ('__________')

        print ('|    |')

        print ('|    O')

        print ('|   \|')

        print ('|    |')

        print ('|')

        print ('|_________')

        print ('')

    elif attempts == 2:

        print ('__________')

        print ('|    |')

        print ('|    O')

        print ('|   \|/')

        print ('|    |')

        print ('|')

        print ('|_________')

        print ('')

    elif attempts == 1:

        print ('__________')

        print ('|    |')

        print ('|    O')

        print ('|   \|/')

        print ('|    |')

        print ('|   /  ')

        print ('|_________')

        print ('')

    else:

        print ('__________')

        print ('|    |')

        print ('|    O')

        print ('|   \|/')

        print ('|    |')

        print ('|   / \ ')

        print ('|_________')

        print ('')



#Win or Fail messages

if attempts:

    print('Congratulations you win. The answer was', word)

else:

    print('You lose. The answer was', word)
