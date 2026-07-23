from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # set up a default dict using a blank list
        groups = defaultdict(list)
        for word in strs:
            ''' loop through all words in strs and do stuff '''
            # create a char with rep sof all 26 lower case letters
            count = [0] * 26
            for char in word:
                ''' go through each char in each word and convert it to a ceasar cypher '''
                count[ord(char) - ord('a')] += 1
            # append to groups 
            groups[tuple(count)].append(word)
        # return list
        return list(groups.values())
        