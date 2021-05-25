word = input().upper()
word_set = set(word)
counts = []

for i in list(word_set):
    counts.append(word.count(i))

if counts.count(max(counts)) > 1:
    print('?')
else:
    word_index = counts.index(max(counts))
    print(list(word_set)[word_index])