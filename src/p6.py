def find_max_occurrence_character(input_string):
    # Create a dictionary to store character frequencies
    char_count = {}
    
    # Remove whitespaces and punctuation, and consider case-sensitivity
    cleaned_string = ''.join(char for char in input_string if char.isalnum())
    
    # Calculate character frequencies
    for char in cleaned_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the character with the maximum occurrence
    max_char = ''
    max_count = 0

    for char, count in char_count.items():
        if count > max_count:
            max_char = char
            max_count = count
    
    return f"Character: '{max_char}', Occurrence: {max_count}"

# Input string
input_string = "Hello, world!"

# Print the result
result = find_max_occurrence_character(input_string)
print(result)
