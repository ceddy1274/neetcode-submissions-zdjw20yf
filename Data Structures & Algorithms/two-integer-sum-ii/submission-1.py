class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer = 0
        leftPointerValue = 0
        rightPointer = len(numbers)-1
        rightPointerValue = 0
        indexSum = 1001

        while(leftPointer <= rightPointer):
            leftPointerValue = numbers[leftPointer]
            rightPointerValue = numbers[rightPointer]
            indexSum = leftPointerValue + rightPointerValue
            if(indexSum < target):
                leftPointer += 1
            elif(indexSum > target):
                rightPointer -= 1
            else:
                return [leftPointer+1, rightPointer+1]
