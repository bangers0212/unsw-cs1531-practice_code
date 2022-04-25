
import string
import re


def similarities(texts, unknown):

    freq_arrays = []
    max_len = 0
    all_texts = texts + [unknown]
    for name in all_texts:
        lens = []
        with open(name, 'r') as file:
            # split the string based of newlines and white-space
            contents = re.split("\n| ", file.read())
            # filter out empty strings
            contents = list(filter(None, contents))
            # filter out punctuations
            for word in contents:
                new_word = word.strip(string.punctuation)
                lens.append(len(new_word))
        set_lens = list(set(lens))
        freq = [lens.count(set_lens[set_lens.index(i)])
                if i in set_lens else 0 for i in range(1, max(lens) + 1)]
        if max(lens) > max_len:
            max_len = max(lens)
        freq_arrays.append(freq)

    # unknown is the final array in freq_arrays
    fix(freq_arrays, max_len)

    check_arrs = freq_arrays[:-1]
    unk_arr = freq_arrays[-1]
    sims = []
    count = 0
    for arr in check_arrs:
        sim = similar(arr, unk_arr, max_len)
        sims.append((sim, texts[count]))
        count += 1

    sims.sort(key=lambda i: i[0], reverse=True)
    return sims


def fix(arrays, max_len):
    for arr in arrays:
        while len(arr) != max_len:
            arr.append(0)


def similar(freq, check, size):
    num = sum(freq[i] * check[i] for i in range(size))
    denom = (sum(freq[i] ** 2 for i in range(size)) ** 0.5) * \
        (sum(check[i] ** 2 for i in range(size)) ** 0.5)
    return round(num/denom, 3)


similarities(['texts/shakespeare.txt', 'texts/austen.txt'],
             'texts/unknown.txt')
