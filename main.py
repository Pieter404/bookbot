from stats import num_words, num_char, sortList

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    word_count = num_words(get_book_text("/home/sarin/projects/bookbot/books/frankenstein.txt"))
    letter_count = num_char(get_book_text("/home/sarin/projects/bookbot/books/frankenstein.txt"))
    sorted_chars = sortList(letter_count)
    print(f"============= BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
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