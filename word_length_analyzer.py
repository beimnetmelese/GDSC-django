def word_length(word_list):
    word_len = []
    for i in range(len(word_list)):
        word_len.append(len(word_list[i]))
    return word_len
def average_word_length(word_list):
    word_len = []
    for i in range(len(word_list)):
        word_len.append(len(word_list[i]))
    sum = 0
    for i in range(len(word_len)):
        sum += word_len[i]
    average = sum / len(word_len)
    return average
def longest_word(text):
    text_split = text.split()
    long_word = text_split[0]
    for i in text_split:
        if len(i) >= len(long_word):
            long_word = i
    longestword = long_word
    longest_length = len(long_word)
    print(f"The longest word is {longestword} and it's length is {longest_length}")
def shortest_word(text):
    text_split = text.split()
    short_word = text_split[0]
    for i in text_split:
        if len(i) <= len(short_word):
            short_word = i
    shortestword = short_word
    shortest_length = len(short_word)
    print(f"The shortest word is {shortestword} and it's length is {shortest_length}")
def word_length_distribuation(text):
    text_split = text.split()
    word_len = []
    word_freq = []
    word_freq_dict = {}
    for i in range(len(text_split)):
        word_len.append(len(text_split[i]))
    for j in word_len:
        word_freq.append(word_len.count(j))
    for z in range(len(word_len)):
        word_freq_dict.update({word_len[z]:word_freq[z]})
    return word_freq_dict
def word_length_distribution_ascending_order(text):
    text_split = text.split()
    word_len = []
    word_freq = []
    word_freq_dict = {}
    for i in range(len(text_split)):
        word_len.append(len(text_split[i]))
    for j in word_len:
        word_freq.append(word_len.count(j))
    for z in range(len(word_len)):
        word_freq_dict.update({word_len[z]: word_freq[z]})
    ascending_order = sorted(word_freq_dict.items())
    print(ascending_order)

