from stats import count_words, count_characters, make_sorted_list
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def print_report(book_path, num_words, sorted_list):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")

  for item in sorted_list:
    if item["char"].isalpha():
      print(f"{item["char"]}: {item["count"]}")

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  book_text = get_book_text(book_path)
  num_words = count_words(book_text)
  chars_dict = count_characters(book_text)
  sorted_list = make_sorted_list(chars_dict)
  print_report(book_path, num_words, sorted_list)

main()