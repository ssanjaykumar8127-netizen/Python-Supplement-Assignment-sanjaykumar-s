# Problem 51: Reverse words in a sentence
# Find and fix the error
def reverse_words(sentence):
    # Split the sentence into words, reverse each word, and join back
    return " ".join(word[::-1] for word in sentence.split())

text = "Hello World"
print(f"Reversed words: {reverse_words(text)}")



