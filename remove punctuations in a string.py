import string

def remove_punctuation(text):
    # Create a translation table that maps punctuation to None
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

# Example usage
input_text = "Hello, world! This is great; isn't it?"
result = remove_punctuation(input_text)
print(result)
