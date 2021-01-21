# Random Sentence Generator by Vahin Sharma

import pandas as pd
import random, re, time

x = pd.read_csv("data.csv")["word"].to_list()
y = pd.read_csv("data.csv")["part"].to_list()

nouns = []
verbs = []
adjectives = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
adverbs = []

for i, j in zip(x, y):
    if j == 1:
        nouns.append(i)
    elif j == 2:
        verbs.append(i)
    elif j == 3:
        adjectives.append(i)
    else:
        adverbs.append(i)

while True:
    secondAdjective = random.choice(adjectives)
    secondNoun = random.choice(nouns)
    secondArticle = ""
    if random.randint(0, 1) == 1:
        secondArticle = "the"
    else:
        if (secondAdjective[0] if len(secondAdjective) > 0 else secondNoun[0]) in "aeiou":
            secondArticle = "an"
        else:
            secondArticle = "a"

    sentence = ["The", random.choice(adjectives), (random.choice(nouns) + ("s" if random.randint(0, 1) == 1 else "")), random.choice(adverbs) if random.randint(0, 1) == 1 else "", random.choice(verbs), secondArticle, secondAdjective, secondNoun]

    print(re.sub(' +', ' ', (" ".join(sentence)).strip()))

    time.sleep(1)
