from stats import get_word_amount, get_chars_dict, sort_char_dict
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def print_report(book_path, num_words, sorted_char_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_dict:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_amount(text)
    char_dict = get_chars_dict(text)
    sorted_char_dict = sort_char_dict(char_dict)
    print_report(book_path, num_words, sorted_char_dict)

main()