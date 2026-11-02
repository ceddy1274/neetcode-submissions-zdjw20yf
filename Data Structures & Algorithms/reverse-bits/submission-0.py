class Solution:
    def reverseBits(self, n: int) -> int:
        binaryString = ""
        while(n != 0):
            if(n % 2 == 1):
                binaryString += '1'
            else:
                binaryString += '0'
            n = n // 2
        binaryString += '0'* (32-len(binaryString))
        num = 0
        mult = 1
        for i in range(len(binaryString)-1, -1, -1):
            if binaryString[i] == '1':
                num += mult
            mult *= 2
        return num
        
