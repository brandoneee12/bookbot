from stats import get_num_words, get_unique_chars, sorted_report
import sys


def get_book_text(file_path):
    try:
        with open(file_path, 'r') as f:
            file_reader = f.read()
            return file_reader
    except FileNotFoundError:
        print(f"Error: Could not find file '{file_path}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(1)

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
read_book = get_book_text(book_path)
print(get_num_words(read_book))

char_counts = get_unique_chars(read_book)
sorted_chars = sorted_report(char_counts)

# Print only alphabetic characters in the expected format
for char_dict in sorted_chars:
    char = char_dict["char"]
    count = char_dict["num"]
    if char.isalpha():  # Only print letters, not spaces or symbols
        print(f"{char}: {count}")
