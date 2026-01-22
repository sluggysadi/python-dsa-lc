# String Manipulation without Built-in Functions

def find_vowels_positions(s)
    vowels = "aeiouAEIOU"
    positions = []
    for index in range(len(s)):
        if s[index] in vowels:
            positions.append(index)
    return positions