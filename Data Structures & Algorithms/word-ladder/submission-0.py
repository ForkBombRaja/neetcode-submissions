class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # convert the list into a set we can use
        wordSet = set(wordList)
        if endWord not in wordSet:
            '''
            if our goal isnt there exit with 0 now
            '''
            return 0
        # create a deque set with begin word
        dq = deque([(beginWord, 1)])
        # use this as our alphabet all 26 lower case
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        while dq:
            '''
            now loop through the word and alter one letter if we find one go then set as somewhere we can go
            if this is in the list move on and if we hit end word we return
            otherwise deque collapses and we return 0
            '''
            word, steps = dq.popleft()
            for char in range(len(word)):
                for letter in alphabet:
                    if letter == word[char]:
                        continue
                    # shift a letter
                    nextWord = word[:char] + letter + word[char + 1:]
                    if nextWord == endWord:
                        return steps + 1
                    if nextWord in wordSet:
                        wordSet.remove(nextWord)
                        dq.append((nextWord, steps + 1))
        return 0   
        