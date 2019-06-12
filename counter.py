# Tally occurrences of words in a list
from collections import Counter
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
Counter({'blue': 3, 'red': 2, 'green': 1})
