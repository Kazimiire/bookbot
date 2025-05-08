import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sort_num_chars

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
    return book_contents

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    word_count = get_num_words(book_contents)
    char_dict = get_num_chars(book_contents)
    sorted_chars = sort_num_chars(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_info in sorted_chars:
        if char_info["char"].isalpha():
            print(f"{char_info['char']}: {char_info['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()