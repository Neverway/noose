def organize(filename):
    with open(filename) as wordlist:
        words = list(wordlist.readlines())

    with open(filename, 'w') as wordlist:
        words = (word.strip() for word in words)
        words = (word.lower() for word in words)
        for word in sorted(set(words)):
            if not word:
                continue
            wordlist.write(word)
            wordlist.write('\n')

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    organize(filename)

