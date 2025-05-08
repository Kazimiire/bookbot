def get_num_words(book_contents):
    words_counter = 0
    split_to_words = book_contents.split()
    for word in split_to_words:
        words_counter += 1
    return words_counter

def get_num_chars(book_contents):
    char_dict = {}
    for char in book_contents.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def sort_num_chars(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        char_info = {"char": char, "num": count}
        chars_list.append(char_info)

    def sort_on(dict):
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list