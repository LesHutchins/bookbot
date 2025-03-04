def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_characters_by_count(char_counts):
    sorted_list = [{"char": char, "count": count} for char, count in char_counts.items() if char.isalpha()]
    sorted_list.sort(reverse=True, key=lambda d: d["count"])
    return sorted_list

"""def count_words(text):
    words = text.split()
    return len(words)"""
