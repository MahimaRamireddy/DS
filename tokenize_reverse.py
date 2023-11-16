def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse each word
    reversed_words = [word[::-1] for word in words]

    # Concatenate the reversed words into a sentence
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

# Example usage
input_sentence = "Hello World, how are you?"
output_sentence = reverse_words(input_sentence)
print(output_sentence)