from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(t) > len(s):
            ''' if either is null or t is bigger than s return empty '''
            return ""
        # needed profile
        need = Counter(t)
        # num of unique chars needed
        required = len(need)
        # make a default dictionary 
        windowCounts = defaultdict(int)
        # number of unique chars satisfied compare rto required
        have = 0                      
        # start and end of best window init at outside array.
        res = [-1, -1]
        # set length                
        resLen = float('inf')
        # init left to 0
        left = 0
        for right, ch in enumerate(s):
            ''' for each right edge and char in enumerate if we have all chars of a certain type increment have '''
            windowCounts[ch] += 1
        
            if ch in need and windowCounts[ch] == need[ch]:
                have += 1
        
            # Try to shrink window from the left while it's still valid
            while have == required:
                ''' as long as things check out and its possible loop and the n try to shrink left and move right until hitting the end of s '''
                # Update result if this window is smaller
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                leftCh = s[left]
                windowCounts[leftCh] -= 1
                if leftCh in need and windowCounts[leftCh] < need[leftCh]:
                    have -= 1
                left += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""        