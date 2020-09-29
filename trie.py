from collections import defaultdict
class Trie:
    def __init__(self):
        TrieNode = lambda: defaultdict(TrieNode)
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.trie
        for i, letter in enumerate(word):
            curr = curr[letter]
            if i == len(word) - 1:
                curr["leaf"] = True


    def search(self, word: str) -> bool:
        curr = self.trie
        for i, letter in enumerate(word):
            if letter not in curr:
                return False
            curr = curr[letter]
            if i == len(word) - 1:
                return curr["leaf"]
        return True


    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for i, letter in enumerate(prefix):
            if letter not in curr:
                return False
            curr = curr[letter]
            if i == len(prefix) - 1:
                return True
        return True
