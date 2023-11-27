paragraph = input("Enter a paragrph: ")
def word_tokenization(word):
    return word.split()
def word_frequency(word):
    split_word = word.split()
    word_freq = {}
    word_freqe = []
    for i in split_word:
        word_freqe.append(split_word.count(i))
    for j in range(len(word_freqe)):
        word_freq.update({split_word[j]:word_freqe[j]})
    return word_freq
def descending_order(word):
    split_word = word.split()
    word_freq = {}
    word_freqe = []
    for i in split_word:
        word_freqe.append(split_word.count(i))
    for j in range(len(word_freqe)):
        word_freq.update({split_word[j]: word_freqe[j]})
    word_ascending_order = sorted(word_freq.items(), key=lambda x:x[1], reverse=True)
    print(word_ascending_order)
def top_frequency(word):
    split_word = word.split()
    word_freq = {}
    word_freqe = []
    for i in split_word:
        word_freqe.append(split_word.count(i))
    for j in range(len(word_freqe)):
        word_freq.update({split_word[j]: word_freqe[j]})
    word_ascending_order = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    numbers = int(input("Enter the top Number frequency: "))
    top_frequency = []
    for i in range(numbers):
        top_frequency.append(word_ascending_order[i])
    print(top_frequency)

def word_search(search):
    word = input("Search: ")
    split_word = search.split()
    word_freq = {}
    word_freqe = []
    for i in split_word:
        word_freqe.append(split_word.count(i))
    for j in range(len(word_freqe)):
        word_freq.update({split_word[j]: word_freqe[j]})
    if word in search:
        searc = word_freq[word]
        print(f"Yes the word '{word}' is found in the paragraph and the frequency of the word is {searc}")
    else:
        print("The word your looking for is Not found!! on the paragraph")


