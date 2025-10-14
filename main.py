from stats import num_words, num_char, sortList
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py </home/sarin/projects/bookbot/books/BOOKNAME>")
        sys.exit(1)
    word_count = num_words(get_book_text(sys.argv[1]))
    letter_count = num_char(get_book_text(sys.argv[1]))
    sorted_chars = sortList(letter_count)
    print(f"============= BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count --------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print(f"=============== END ==============")

main()