from stats import count_words, count_characters, make_sorted_list

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  book_path = "./books/frankenstein.txt"
  book_text = get_book_text(book_path)
  num_words = count_words(book_text)
  chars_dict = count_characters(book_text)
  sorted_list = make_sorted_list(chars_dict)

main()