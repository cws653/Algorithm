from collections import defaultdict
a = ["eat","tea","tan","ate","nat","bat"]
anagram = defaultdict(list)

for word in a:
    anagram[''.join(sorted(word))].append(word)

print(anagram.values())