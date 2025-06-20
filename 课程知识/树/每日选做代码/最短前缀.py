class Treenode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.count = 0

words = []
try:
    while True:
        line = input()
        if line.strip():
            words.append(line.strip())
except EOFError:
    pass


root = Treenode('')
for word in words:
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = Treenode(char)
        node = node.children[char]
        node.count += 1


prefixes = {}
for word in words:
    node = root
    prefix = ''
    for char in word:
        prefix += char
        node = node.children[char]
        if node.count == 1:
            break
    prefixes[word] = prefix


for word in words:
    print(f"{word} {prefixes[word]}")




#法二：直接搜索

words = []
while True:
    try:
        words.append(input())
    except EOFError:
        break
n = len(words)
sorted_words = sorted(words)
buffer = set()
pre_dict = dict()
for i, w in enumerate(sorted_words):
    for j in range(len(w)):
        pre = w[:j+1]
        if (pre in buffer):
            continue
        if i+1 < n and sorted_words[i+1].startswith(pre):
            buffer.add(pre)
        else:
            break
    pre_dict[w] = w[:j+1]
for w in words:
    print(w, pre_dict[w])
