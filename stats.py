def get_word_amount(text):
    amountOfWords = text.split()
    num_words = len(amountOfWords)
    return num_words

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]
    
def sort_char_dict(dict):
    sortable_list = []
    for char in dict:
        sortable_list.append({"char": char, "num": dict[char]})
    sortable_list.sort(reverse=True, key=sort_on)    
    return sortable_list
