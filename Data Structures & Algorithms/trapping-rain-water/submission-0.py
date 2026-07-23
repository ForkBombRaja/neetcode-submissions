class Solution:
    def trap(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        # start with the left at far left of frame
        left = 0
        # start with right at far right at frame
        right = len(height) - 1
        # start with no water (left)
        leftMax = 0
        # start with no water (right)
        rightMax = 0
        # start with no water (accumulated)
        water = 0
        while left < right:
            ''' while the left and right pointers are seperate keep looping '''
            if height[left] > leftMax:
                ''' if right height  is higher than our leftmax update  max left '''
                leftMax = height[left]
            if height[right] > rightMax:
                ''' if right height is higher than our current max heighht update max right '''
                rightMax = height[right]

            if leftMax < rightMax:
                ''' if left max smaller than right max then add the value of the left wall minus the floor move left rightwards '''
                water += leftMax - height[left]
                left += 1
            else:
                ''' if right max smaller than right max then add the value of the right wall minus the floor then move righr leftwards'''
                water += rightMax - height[right]
                right -= 1
        return water