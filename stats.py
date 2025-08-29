def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def wordcount(book_text): 
    count = 0 
    book_words = book_text.split()
    for word in book_words:
        count += 1
    return f"Found {count} total words"

def char_occurances(book_text):
    book_text = book_text.lower()
    book_text = book_text.split()
    chars = {}
    #chars = {" ": len(book_text)} #logs spaces if wanted
    for words in book_text:
        for char in words:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def list_dicts(chars):
    new_chars = []
    for char, num in chars.items():
        new_chars.append({"char": char, "num": num})
   # print(new_chars)
    return new_chars

def sort_key(key):
    return key["num"]