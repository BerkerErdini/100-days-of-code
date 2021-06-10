# https://leetcode.com/problems/shuffle-the-array/submissions/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        array = nums
        partA = array[:n]
        partB = array[n:]
        shuffledArray = []

        for i in range(n):
            shuffledArray.append(partA[i])
            shuffledArray.append(partB[i])

        return shuffledArray