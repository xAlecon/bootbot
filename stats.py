def word_counter(text):
    return len(text.split())

def character_counter(text):
    char_counts = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return (char_counts)

def sort_on(d):
    return d["num"]

# This sorts the list like this - ("b", "num": 4868)
def letter_sort(num_chars_list):
    sorted_list = []
    for ch in num_chars_list:
        sorted_list.append({"char": ch, "num": num_chars_list[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
