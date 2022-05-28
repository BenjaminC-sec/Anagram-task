# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    first_value = input("Enter the first string: ")
    second_value = input("Enter the second string: ")
    if sorted(first_value) == sorted(second_value):
        print("They are anagrams.")
    else:
        print("They are not anagrams.")


find_anagram('word', 'anagram')
