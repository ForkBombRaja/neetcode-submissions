from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # we use a deque as a window
        window = deque()
        # we store the maxes here
        windowMaxes = []

        for num in range(len(nums)):
            ''' loop through nums isolate the window remove smaller elements
            and add the current max to deque then the windowMaxes '''
            if window and window[0] <= num - k:
                window.popleft()
            while window and nums[window[-1]] <= nums[num]:
                window.pop()
            window.append(num)
            if num >= k - 1:
                windowMaxes.append(nums[window[0]])

        return windowMaxes  