class Solution:
    indexes = []
    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += word
            self.indexes.append(len(word))
        return s
    def decode(self, s: str) -> List[str]:
        i = 0
        words = []
        length = 0
        while self.indexes:
            curr = self.indexes.pop(0)
            length = curr + length
            print("Length: ", length)
            print("i: ", i)
            word = ""
            for index in range(i, length):
                print("Index: ", index)
                word += s[index]
            words.append(word)
            i += curr
            
        return words