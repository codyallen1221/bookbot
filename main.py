import sys
from stats import count_characters

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

from stats import get_num_words
from stats import make_char_list

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_counts = count_characters(book_text)
    char_list = make_char_list(char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in char_list:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

main()