import sys
from stats import count_words, count_characters, sort_characters_by_count

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    sorted_char_counts = sort_characters_by_count(count_characters(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_char_counts:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()

"""from stats import count_words, count_characters, sort_characters_by_count

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def main():
    relative_path = "books/frankenstein.txt"
    book_text = get_book_text(relative_path)
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_char_counts=sort_characters_by_count(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_char_counts:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()"""

"""from stats import count_words

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def main():
    relative_path = "books/frankenstein.txt"
    book_text = get_book_text(relative_path)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document.")

if __name__ == "__main__":
    main()"""

"""def get_book_text(filepath):
    with open (filepath, 'r') as file:
        return file.read()

def main():
    relative_path="books/frankenstein.txt"
    book_text=get_book_text(relative_path)
    print("\n" + book_text)

if __name__=="__main__":
    main()"""
