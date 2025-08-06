# Input sentence
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Sort the words alphabetically (case-insensitive)
words.sort(key=str.lower)

# Print the sorted words
print("Sorted sentence:")
print(" ".join(words))
