def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_number_of_words(filepath):
    file_contents = get_book_text (filepath)
    split_text = file_contents.split()
    number_of_words = 0
    for word in split_text:
        number_of_words += 1
    return number_of_words

def get_number_of_charaters(filepath):
    file_contents = get_book_text (filepath)
    file_contents_low = file_contents.lower()
    charater_number = {}
    for character in file_contents_low:
        if character in charater_number:
            charater_number[character] += 1
        else:
            charater_number[character] = 1
    return charater_number


def sort_on(items):
    return int(items[1])


def sort_charaters(character_numbers):
    char_list = list(character_numbers.items())
    char_list.sort(reverse=True, key=sort_on)
    return char_list




