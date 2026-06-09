class Node:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Node()
            curr = curr.children[letter]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node

            for i in range(index, len(word)):
                letter = word[i]
                if letter == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    print(letter)
                    if letter not in curr.children:
                        return False
                    curr = curr.children[letter]
            print()
            return curr.endOfWord
        return dfs(0, self.root)
