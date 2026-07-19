# Ques: Reverse the order of words in the sentence.
# Output: "powerful and fun is Python"

# you have a sentence

sentence ="Python is fun and powerful"

# Python Code:
# Split() breaks the sentence into words
# [::-1] reverses the word list
# ' '.join() put them back into string

reversed_sentence = ' '.join(sentence.split()[::-1])
print(reversed_sentence)
