with open('story.txt', 'r') as f:
    story = f.read()

words = set()

start_of_word = -1

target_start = '('
target_end = ')'

for index, char in enumerate(story):
    if char == target_start:
        start_of_word = index

    if char == target_end and start_of_word != -1:
        word = story[start_of_word:index + 1]
        words.add(word)

answer = {}

print()
for word in words:
    answers = input("Enter a word for " + word + ": ")
    story = story.replace(word, answers)

print()
print(story)