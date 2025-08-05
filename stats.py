def num_words(book_text):
    count = 0
    for word in book_text.split():
        count += 1
    return count

def num_char(book_text):
    letterCount = {}
    for char in book_text:
        char = char.lower()
        if char in letterCount:
            letterCount[char] += 1
        else:
            letterCount[char] = 1
    return letterCount