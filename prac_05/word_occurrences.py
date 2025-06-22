# Get user input
text = input("Text: ")
#Splitting and statistics
words = text.split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

max_word_length = max(len(word) for word in word_counts) if word_counts else 0

# Print sorted results with aligned columns
for word in sorted(word_counts):
    print(f"{word:{max_word_length}} : {word_counts[word]}")
#1hour
