import sys
from stats import get_num_words, chars_count, sorted_list_from_dict, report

def get_args():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception as e:
        print(f"Error during reading the file: {e}")


def main():
    book_path = get_args()
    book_content = get_book_text(book_path)
    chars_count_result = chars_count(book_content)
    sorted_list = sorted_list_from_dict(chars_count_result)
    word_count_result = get_num_words(book_content)

    report(word_count_result, sorted_list, book_path)


main()
