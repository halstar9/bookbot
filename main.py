import sys

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()
    
from stats import get_num_words
from stats import get_num_characters
from stats import sort_by_num_of_characters

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    frankenstein = get_book_text(path)
    word_count = get_num_words(frankenstein)
    char_count = get_num_characters(frankenstein)
    sorted_chars = sort_by_num_of_characters(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {len(word_count)} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['num']}")
    
    print("============= END ===============")


main()