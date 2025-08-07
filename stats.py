def get_num_words(text):
    num_words = text.split()
    return f'Found {len(num_words)} total words'

def get_unique_chars(text):
    chars = {}
    text_lower = text.lower()
    for char in text_lower:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def get_count(char_dict):
    # Helper function to get the count from a character dictionary
    return char_dict["num"]

def sorted_report(chars):
    # Convert dictionary to list of dictionaries
    char_list = []
    for char, count in chars.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)

    # Sort by count from greatest to least
    char_list.sort(key=get_count, reverse=True)

    return char_list
