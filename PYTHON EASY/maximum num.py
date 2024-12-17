def max_words_in_sentence(text):
    # Split the text into sentences
    sentences = text.split('.')
    
    max_words = 0  # Initialize the maximum word count
    
    # Iterate through each sentence
    for sentence in sentences:
        # Strip leading/trailing whitespace and split the sentence into words
        words = sentence.strip().split()
        # Update max_words if the current sentence has more words
        max_words = max(max_words, len(words))
    
    return max_words

def main():
    # Input from the user
    text = input("Enter text containing multiple sentences: ")
    
    # Get the maximum number of words in a single sentence
    result = max_words_in_sentence(text)
    
    print(f"The maximum number of words in a single sentence is: {result}")

if __name__ == "__main__":
    main()
