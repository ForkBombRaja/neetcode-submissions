class MedianFinder:

    def __init__(self):
        """
        initalizes a median finder
        """
        # set up empty data wherw we store as negs
        self.neg = []
        # set up empty data wherw we store as poses
        self.pos = []


    def addNum(self, num: int) -> None:
        """
        :type num: int
        :rtype: None
        """
        # add to small first as a negative 
        heapq.heappush(self.neg, -(num))
        # shift from neg to pos to adjust adding 1 more num
        heapq.heappush(self.pos, -(heapq.heappop(self.neg)))
        if len(self.neg) < len(self.pos):
            ''' if negs is bigger shift one over  to maintain condition neg >= pos'''
            heapq.heappush(self.neg, -(heapq.heappop(self.pos)))

    def findMedian(self) -> float:
        """
        :rtype: float
        """
        if len(self.neg) > len(self.pos):
            ''' if neg is bigger then this is odd return middle num
            else it is even length return mean of middle 2 '''
            return float(-self.neg[0])
        else:
            return float((-self.neg[0] + self.pos[0]) / 2.0)
        
        