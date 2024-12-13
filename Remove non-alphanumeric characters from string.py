#Write a Python program to remove all non-alphabetic characters from a string.
# Take user input for the string
user_input = input("Enter a string: ")

# Initialize an empty string to store the result
result = ""

# Loop through each character in the input string
for char in user_input:
    # Check if the character is alphabetic
    if char.isalpha():
        # If it is alphabetic, add it to the result string
        result += char

# Output the result
print("String after removing non-alphabetic characters:", result)
