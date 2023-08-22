import re

def are_anagrams(str1, str2):
    # Remove whitespace and punctuation, and convert to lowercase
    str1 = re.sub(r'[^a-zA-Z]', '', str1).lower()
    str2 = re.sub(r'[^a-zA-Z]', '', str2).lower()

    # Check if the sorted characters in both strings are the same
    return sorted(str1) == sorted(str2)

# Examples
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("debit card", "Bad credit")) # True  
print(are_anagrams("hello", "bye")) # False
print(are_anagrams("restful", "fluster"))  # Should be True? Their count of each character are same
print(are_anagrams("listen", "silentt"))  # False
print(are_anagrams("Conversation", "Voices, rant on")) # True
