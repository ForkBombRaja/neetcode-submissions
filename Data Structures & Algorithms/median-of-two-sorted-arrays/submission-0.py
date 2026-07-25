class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # merge the two arrays and make sure its sorted
        merged = sorted(nums1 + nums2)
        # index of median within merged
        medianIndex = (len(nums1)+ len(nums2))//2
        # median
        median = 0
        if ((len(nums1)+len(nums2)) % 2) == 1:
            ''' if odd length set middle as median 
            otherwise use avg of two middles
            '''
            median = merged[medianIndex]
        else:
            median = (merged[medianIndex - 1] + merged[medianIndex]) / 2.0
        return median