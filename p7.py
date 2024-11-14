print("Name: Niya Joshy")
print("Admission No:A24MCA049")
print("Experiment No:7")

from collections import Counter

def character_frequency(s):
    return Counter(s)

def modify_string(s):
    if s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'

input_string =input("enter a word :")
frequency = character_frequency(input_string)
modified_string = modify_string(input_string)

print("Character Frequency:", frequency)
print("Modified String:", modified_string)

def longest_word_length(words):
    if not words:
        return 0
    return max(len(word) for word in words)

user_input = input("Enter a list of words separated by spaces: ")
word_list = user_input.split()
longest_length = longest_word_length(word_list)
print("Length of the longest word:", longest_length)






