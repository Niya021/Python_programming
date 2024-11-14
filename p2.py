print("Name: Niya Joshy")
print("Admission No:A24MCA049")
print("Experiment No:2")

text = input("Enter a line of text: ")
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
for word, count in word_count.items():
    print(word + ":" + str(word_count[word]))

if len(words)>0:
    first_word = words[0]

    if len(first_word) > 1:
        modified_first_word = (
                first_word[-1] + first_word[1:-1] + first_word[0]
        )
    else:
        modified_first_word = first_word

    print("Modified first word is " ,modified_first_word)
