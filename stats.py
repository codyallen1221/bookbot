def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def make_char_list(char_counts):
    char_list = []
    for char, count in char_counts.items():
        entry = {"char": char, "num": count}
        char_list.append(entry)
    char_list.sort(key=lambda entry: entry["num"], reverse=True)
    return char_list