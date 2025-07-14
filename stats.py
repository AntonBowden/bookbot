def count_words(text):
  return len(text.split())

def count_characters(text):
  result = {}
  for char in text:
    char = char.lower()
    if char not in result:
      result[char] = 1
    else: result[char] += 1
  return result

def sort_on(items):
  return items["count"]

def make_sorted_list(dict):
  result = []
  for char in dict:
    result.append({"char": char, "count": dict[char]})

  result.sort(reverse=True, key=sort_on)

  return result