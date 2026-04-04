class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        if nums == [0, 0, 0]:
            final.append(nums)
            return final
        #seperate between positive and negative numbers
        pos = []
        neg = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        for i in range(len(pos)):
            for j in range(len(pos)):
                if i != j:
                    res = -(pos[i] + pos[j])
                    if res in neg:
                        triplets = [pos[i], pos[j], res]
                        triplets.sort()
                        if triplets not in final:
                            final.append(triplets)
        for i in range(len(neg)):
            for j in range(len(neg)):
                if i != j:
                    res = -(neg[i] + neg[j])
                    if res in pos:
                        triplets = [neg[i], neg[j], res]
                        triplets.sort()
                        if triplets not in final:
                            final.append(triplets)
        return final
