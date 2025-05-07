def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
    return book_contents

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    print(book_contents)


if __name__ == "__main__":
    main()