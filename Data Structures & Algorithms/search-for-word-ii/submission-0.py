class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # empty trie
        root = TrieNode()
        for word in words:
            ''' build a trie including all words in words '''
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
        # get num rows
        rows = len(board)
        # get num cols
        cols = len(board[0])
        # initialize a empty result
        result = []
        def backtrack(row, col, node):
            """
            backtrack on a trie based on a speific board pos
            """
            # find the letter specified 
            letter = board[row][col]
            if letter not in node.children:
                ''' if the letter isnt adjacent bail kill recursion '''
                return
            # get the next letter
            node = node.children[letter]
            if node.word:
                ''' if the word follws in node set word into results and nullify   node'''
                result.append(node.word)
                node.word = None
            # kill char
            board[row][col] = "#"
            for dRow, dCol in [(1,0), (-1,0), (0,1), (0,-1)]:
                ''' if char in adjacent recurse '''
                nRow = row + dRow
                nCol = col + dCol
                if (0 <= nRow < rows and 0 <= nCol < cols and board[nRow][nCol] != "#"):
                    backtrack(nRow, nCol, node)
            # reset char
            board[row][col] = letter
        for row in range(rows):
            ''' check each char using bactrack func '''
            for col in range(cols):
                backtrack(row, col, root)
        return result
class TrieNode:
    """
    This class creates a node in a Trie to solve the Word Search II problem
    """
    def __init__(self):
        """ initializes a node """
        # no children yet but have a trie downlist set up
        self.children = {}
        # insert word here if it hits
        self.word = None        