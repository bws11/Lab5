with open('story.txt', 'r') as f:
    content = f.read()

words = content.split(' ')
word_count = len(words)

print(f"The word count is {word_count}")