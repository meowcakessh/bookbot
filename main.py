from stats import wordcount, char_occurances, list_dicts, sort_key, get_book_text
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
   
    print("============ BOOKBOT ============",
        f"\nAnalyzing book found at {sys.argv[1]}...",
        "\n----------- Word Count ----------")
    print(wordcount(get_book_text(sys.argv[1])))
    print("--------- Character Count -------")

    char_list = list_dicts(char_occurances(get_book_text(sys.argv[1])))
    char_list.sort(key=sort_key, reverse=True)

    for char in char_list:
        ch = char["char"]
        print(f"{ch}: {char['num']}")

if __name__ == '__main__':
    main()