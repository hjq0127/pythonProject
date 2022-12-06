"""
CP1404/CP5632
Write a program to count the occurrences of words in a string.
"""
Word = {}
Usertype = input("Text:")
Words = Usertype.split(' ')
for i in Words:
    frequency = Word.get(i, 0)
    Word[i] = frequency + 1
Words = list(Word.keys())
Words.sort()

max_length = max((len(i) for i in Words))
for i in Words:
    print(f"{i:{max_length}} : {Word[i]}")

