class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # make empty list of window maximums
        windowMaxes = []
        # left end of window(inclusive) 
        leftWindow = 0
        # right end of window(excluxive)
        rightWindow = k
        while rightWindow <= len(nums):
            ''' add maxes of window to WindowMaxes keep advancing window right until right end of window hits right end of nums '''
            windowMaxes.append(max(nums[leftWindow:rightWindow]))
            leftWindow+=1
            rightWindow+=1
        return windowMaxes   