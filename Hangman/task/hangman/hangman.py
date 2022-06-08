import random


def hangman_game():
    global wins
    global loses
    global words_to_guess

    word = words_to_guess[random.randint(0, 3)]
    hint = ((len(word)) * '-')
    used_letters = set()
    remaining_guesses = 8

    while remaining_guesses != 0:
        print()
        print(hint)
        if hint == word:
            print('You guessed the word {0}!'.format(word))
            print('You survived!')
            wins += 1
            break

        guess = input('Input a letter:')
        if len(guess) != 1:
            print('Please, input a single letter.')
        elif guess.isupper() or not guess.isalpha():
            print('Please, enter a lowercase letter from the English alphabet.')
        else:
            if guess in used_letters:
                print("You've already guessed this letter.")
                continue
            used_letters.add(guess)
            if guess in word:
                for i in range(0, len(word)):
                    if hint[i] == guess:
                        print('No improvements.')
                        remaining_guesses -= 1
                        break
                    if word[i] == guess:
                        hint = hint[:i] + guess + hint[i + 1:]
            else:
                print("That letter doesn't appear in the word.")
                remaining_guesses -= 1
    if remaining_guesses == 0:
        print('You lost!')
        loses += 1


words_to_guess = ('python', 'java', 'swift', 'javascript')
wins = 0
loses = 0
exit_game = False

print('H A N G M A N')
while not exit_game:
    command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if command == 'play':
        hangman_game()
    elif command == 'results':
        print('You won: {0} times'.format(wins))
        print('You lost: {0} times'.format(loses))
    elif command == 'exit':
        exit_game = True
