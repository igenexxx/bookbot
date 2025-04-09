def get_num_words(text):
    return len(text.split())

def chars_count(text):
    result = dict()

    for c in list(text):
        result[c.lower()] = result.get(c.lower(), 0) + 1

    return result

def sort_on(d):
    return d["count"]

def sorted_list_from_dict(count_stat):
    result = list()

    for k in count_stat:
        if k.isalpha():
            result.append({ "key": k, "count": count_stat[k] })

    result.sort(reverse=True, key=sort_on)

    return result

def report(word_counts, counts_dict_list, path):
    print("=" * 12 + " BOOKBOT " + "=" * 12)
    print(f"Analyzing book found at {path}...")
    print("-" * 11 + " Word Count " + "-" * 10)
    print(f"Found {word_counts} total words")
    print("-" * 9 + " Character Count " + "-" * 7)
    for char_stat in counts_dict_list:
        print(f"{char_stat['key']}: {char_stat['count']}")


