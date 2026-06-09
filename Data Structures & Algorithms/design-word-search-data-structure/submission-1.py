class Node:
    
    def __init__(self):
        self.letters = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.start = Node()

    def addWord(self, word: str) -> None:
        curr = self.start

        for letter in word:
            if letter not in curr.letters:
                curr.letters[letter] = Node()
            curr = curr.letters[letter]    
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.letters.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.letters:
                        return False
                    curr = curr.letters[c]
            return curr.endOfWord
        return dfs(0, self.start)

