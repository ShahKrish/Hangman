import random

movie = ('iron man','captain america','thor','ant man','avengers infinity war'
         ,'avengers endgame','guardians of the galaxy','avengers','avengers age of ultron','spiderman')
chances = 7

name=input('Whats your name?')
print('Hello', name, ',', 'Time to play HANGMAN: MARVEL EDITION!')

def letters(word):
    return list(word)


guess = random.choice(movie)
answer = letters(guess)
char = ""
length=(len(guess))
print('There are', length, 'letters in the movie you have to guess')
print('You have 7 chances to guess the movie. Type in a letter you think is in the movie.')
print('Once You enter the name of the entire movie the game will be over. Good Luck!')
i = ""

while chances > 0 and char.lower() != guess:
    char = input("ENTER HERE")
    if char.lower() == guess:
        print("CONGRATULATIONS, YOU WON!")
    elif char.lower() in guess:
        if answer.count(char.lower()) == 1:
            print('This is letter No.', answer.index(char.lower()) + 1, "of the movie")
        elif answer.count(char.lower()) > 1:
            for i in range(length):
                if answer[i] == char.lower():
                    print('This is letter No.', i+1, 'of the movie')
    else:
        chances = chances - 1
        print('Try again.You have', chances, 'chances left')
    if chances == 0:
        print('SORRY, YOU LOST:(')
