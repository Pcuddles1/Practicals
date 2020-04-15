word_with_count = {}
word_parts = []
lengths = []
longest = 0

text = str(input("enter sentence: "))
word_parts = text.split(' ')

for word in word_parts:  # tests each word in word_parts list
    length = 0
    for letter in word:  # tests each letter in each word
        length = length + 1
    if length > longest:
        longest = length  # this allows for the formatting to be the correct length for any length word
    lengths.append(length)  # adds length into lengths list
    word_with_count = dict(
        zip(word_parts, lengths))  # puts the word and the lenght of that word together into dictionary

list = [(word, length) for word, length in word_with_count.items()]  # converts to list to sort with both key and value
words_sorted = sorted(list)  # sorts list

for word, number in words_sorted:
    print("{:{}} : {}".format(word, longest, number))  # formats prints