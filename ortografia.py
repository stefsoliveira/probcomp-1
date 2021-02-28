def adjust_distance(word, word_on_dic):
    arr = []
    arr.append([i for i in range(len(word_on_dic) + 1)])
    for i in range(1, len(word) + 1):
        arr.append([])
        for j in range(len(word_on_dic) + 1):
            if j == 0:
                arr[i].append(i)
            else:
                if word[i - 1] == word_on_dic[j - 1]:
                    arr[i].append(arr[i - 1][j - 1])
                else:
                    arr[i].append(min(arr[i][j - 1], arr[i - 1][j - 1], arr[i - 1][j]) + 1)
    return arr[len(word)][len(word_on_dic)]


def find_words(words_to_analyze, dictionary):
    for word in words_to_analyze:
        final_words = []
        for word_on_dic in dictionary:
            if len(word_on_dic) >= len(word) - 2 and len(word_on_dic) <= len(word) + 2:
                if len(word_on_dic) >= len(word) - 2 and len(word_on_dic) <= len(word) + 2:
                    distance = adjust_distance(word, word_on_dic)
                    if distance <= 2:
                        final_words.append(word_on_dic)
        space = ' '
        print(space.join(final_words))


words_number = input().split()
# words_number[0] = number of words within a dictionary  (1<=N<=1000)
# words_number[1] = number of words to be analyzed (1<=M <=100)

dictionary = [0]*int(words_number[0])
for i in range(int(words_number[0])):
    dictionary[i] = input()

words_to_analyze = [0]*int(words_number[1])
for i in range(int(words_number[1])):
    words_to_analyze[i] = input()

find_words(words_to_analyze, dictionary)