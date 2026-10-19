class Solution:
    def countBits(self, n: int) -> List[int]:
        def convertToBinary(n):
            binaryNumber = ""
            while(n != 0):
                if (n % 2 == 0):
                    binaryNumber = "0" + binaryNumber
                else:
                    binaryNumber = "1" + binaryNumber
                n //= 2
            return binaryNumber

        bitCount = []
        for i in range(n+1):
            currBinaryNumber = convertToBinary(i)
            bitCount.append(currBinaryNumber.count('1'))
        return bitCount
                
