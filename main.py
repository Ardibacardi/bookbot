def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letters = get_letter_count(text)
    sorted_letters = sort_on(letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words were found in the document")
    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times")
    print('--- End report ---')


def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()

            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def sort_on(Dict):
    sorted_list = sorted(Dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
