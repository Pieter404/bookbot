from stats import num_words, num_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    word_count = num_words(get_book_text("/home/sarin/projects/bookbot/books/frankenstein.txt"))
    letter_count = num_char(get_book_text("/home/sarin/projects/bookbot/books/frankenstein.txt"))
    print(f"{word_count} words found in the document")
    print(letter_count)

main()