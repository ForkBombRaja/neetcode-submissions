class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        :type heights: List[int]
        :rtype: int
        """
        # keep bars here to compare
        barStack = []
        # best area  
        maxArea = 0
        # flag to empty stack at the end 
        heights.append(0)
        for i, h in enumerate(heights):
            ''' loop through heights and when we max out the rect make a area and take max area between them  
            '''
            while barStack and heights[barStack[-1]] > h:
                ''' when we hit a smaller rect then we begin with we make an area to compare
                '''
                height = heights[barStack.pop()]
                if barStack:
                    width = i - barStack[-1] - 1
                else:
                    width = i
                maxArea = max(maxArea, height * width)
            # append the max for this round 
            barStack.append(i)
        return maxArea 