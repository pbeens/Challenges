'''
In response to the challenge introduced in the Google+ Coding Puzzles community,
at http://goo.gl/xkaqM

The original stub for this program can be found at
https://gist.github.com/naomik/5903943
in Javascript.

A successful solution should print ["hello", "cruel", "world", "bears"]
'''

words = ["lazy", "crackers", "hello", "cruel", "world", "bears", "need", "not", "apply"]
puzzle = "\
rbfxw\
hello\
oahcr\
cruel\
vsufd"

def solve (puzzle, words):
    foundWords = []
    for word in words:
        for i in range (0, len(puzzle)):
            if word == puzzle[i:i+len(word)] or word == puzzle[i:i+len(word)*5:5]:
                foundWords.append(word)
    return foundWords


print (solve(puzzle, words))
