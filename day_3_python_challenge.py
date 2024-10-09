# Ask user for text and make all letters lowercase
text = input("Insert a text: ").lower()
# Ask user for 3 letters and make all letters lowercase
letter1 = input("Input a random letter: ").lower()
letter2 = input("Input another random letter: ").lower()
letter3 = input("Input a third random letter: ").lower()
# Store user's letters in a list
letters_list = [letter1, letter2, letter3]
print(letters_list)
# Count how many times the user's 3 letters appear in the textabc
for letter in letters_list:
    print(text.count(letter))
# Convert user's text into a list
user_text_list = list(text)
print(user_text_list)
# Find the length of the list containing the user's text
print(len(user_text_list))
# Find the first letter in the list containing the user's text
print(user_text_list[0])
# Find the last letter in the list containing the user's text
print(user_text_list[-1])
# Invert the order of the elements in the list containing the user's text
reversed_text = user_text_list[::-1]
print(reversed_text)
# Join these elements in the list containing the user's text with spaces in between
joined_reversed_user_text = " ".join(reversed_text)
print(joined_reversed_user_text)
# Check if the word "python" is in the text with a boolean and display the result to the user
print("python" in user_text_list)