import random

WORDLIST = [
    'potato',
    'apple',
    'cat',
    'dog',
    'flag',
    'bathroom',
    'coat',
    'goat',
]

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'.lower()


def main(target, limit=8, multiguess=False):
    target_word = target.strip().lower()
    guess = []
    print(f'Guess the word (it has {len(target_word)} letters)')
    unmasked = set(target_word).difference(ALPHABET)
    while set(target_word).difference(guess).difference(unmasked):
        letters = input(f'{mask_word(target_word, guess, unmasked)}  > ').lower()
        if len(letters) > 1:
            if multiguess:
                letters = list(letters)
            else:
                if target_word.lower() != letters.lower():
                    print('You have chosen poorly...')
                    break
                else:
                    guess.extend(letters)
                    letters = []
        for letter in letters:
            if len(letter) != 1:
                print('You must guess one and only one letter at a time')
                continue
            if letter not in ALPHABET:
                print('You must pick a letter from A to Z')
                continue
            if letter in guess:
                if not multiguess or len(letters) == 1:
                    print('You have already guessed that letter')
                    print(f'Letters already used: {sorted(set(guess))}')

            guess.append(letter)
        wrong_letters = set(guess).difference(target_word)
        if len(wrong_letters) >= limit:
            print(f'You lose! Too many wrong letters: {sorted(wrong_letters)}')
            print(f'The word was {target_word}')
            break
    else:
        print(target_word)
        print('You win!')


def mask_word(word, guess, nomask=''):
    def show_letter(x, guess, nomask):
        return x if x in guess or x in nomask else '.'
    result = [
        show_letter(letter, guess, nomask)
        for letter in word
    ]
    return ''.join(result)

def get_wordlist(filename):
    with open(filename) as wordlist:
        return list(wordlist.readlines())

if __name__ == '__main__':
    import sys
    filenames = sys.argv[1:]
    wordlist = []
    for filename in filenames:
        print(f'Reading words from {filename}')
        wordlist.extend(get_wordlist(filename))
    
    main(random.choice(wordlist or WORDLIST))

