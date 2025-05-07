def get_num_words(book):
    num_words = book.split()
    return num_words

def get_num_characters(book):
    num_characters = {}
    text = book.lower()

    for char in text:
        if char in num_characters:
            num_characters[char] += 1
        else:
            num_characters[char] = 1
    return num_characters

def sort_on(dict):
    return dict["num"]

def sort_by_num_of_characters(num_characters):
    my_list = []
    for key, value in num_characters.items():
        new_dict = {"char": key, "num": value}
        my_list.append(new_dict)
    my_list.sort(reverse=True, key=sort_on)
    return my_list


