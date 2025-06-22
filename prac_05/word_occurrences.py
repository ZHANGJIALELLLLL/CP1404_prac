# Get user input
text = input("Text: ")



# Print sorted results with aligned columns
for word in sorted(word_counts):
    print(f"{word:{max_word_length}} : {word_counts[word]}")
