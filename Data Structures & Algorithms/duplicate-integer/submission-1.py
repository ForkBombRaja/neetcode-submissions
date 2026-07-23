class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        # stuff we've seen
        seen = set()
        for num in nums:
            ''' loop through nums and check if weve seen it
            if we did then return True if not ad to seen '''
            if num in seen:
                return True
            seen.add(num)
        # if we havent returned True yet, return False
        return False