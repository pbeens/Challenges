'''
From https://goo.gl/s3VJAN

Description

Software like Swype and SwiftKey lets smartphone users enter text by dragging their finger over the on-screen keyboard, rather than tapping on each letter.
Example image of Swype: http://www.swype.com/content/uploads/2014/09/swype_path.png
You'll be given a string of characters representing the letters the user has dragged their finger over.
For example, if the user wants "rest", the string of input characters might be "resdft" or "resert".
Input

Given the following input strings, find all possible output words 5 characters or longer.
qwertyuytresdftyuioknn
gijakjthoijerjidsdfnokg

Output

Your program should find all possible words (5+ characters) that can be derived from the strings supplied.
Use http://norvig.com/ngrams/enable1.txt as your search dictionary.
The order of the output words doesn't matter.
queen question
gaeing garring gathering gating geeing gieing going goring

Notes/Hints

Assumptions about the input strings:
QWERTY keyboard
Lowercase a-z only, no whitespace or punctuation
The first and last characters of the input string will always match the first and last characters of the desired output word
Don't assume users take the most efficient path between letters
Every letter of the output word will appear in the input string

Bonus

Double letters in the output word might appear only once in the input string, e.g. "polkjuy" could yield "polly".
Make your program handle this possibility.
'''

'''
NOT WORKING YET...
'''

import urllib.request

words = []
possible_words = []

url = 'https://raw.githubusercontent.com/pbeens/challenges/master/cleandict.txt'
response = urllib.request.urlopen(url)
data = response.readlines()

# create list of words
for line in data:
    words.append(line.strip().decode('UTF-8'))

# find possible words
swype = 'qwertyuytresdftyuioknn'
for word in words:
    if len(word) > 4 and word[0] == swype[0] and word[-1:] == swype[-1:]:
        possible_words.append(word)

print (possible_words)

for word in possible_words:
    possible = True
    for c in word:
        if c not in swype:
            print (c)
            possible = False
    if possible == False:
        possible_words.remove(word)

print (possible_words)


