class Trie():
    def __init__(self):
        self.children = {}
        self.end = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = Trie()
                node = node.children[char]
            
            node.end = w # mark completion of the word
        
        # access the board
        rows, cols = len(board), len(board[0])
        res = set() # set avoid duplicates

        # helper for backtrack
        def backtrack(r, c, node):
            # base case
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == '#' or board[r][c] not in node.children):
                return

            char = board[r][c]
            curr_node = node.children[char]

            if curr_node.end:
                res.add(curr_node.end)
                curr_node.end = None # remove to avoid duplicates
            
            # visited
            board[r][c] = '#'

            backtrack(r + 1, c, curr_node)
            backtrack(r - 1, c, curr_node)
            backtrack(r, c + 1, curr_node)
            backtrack(r, c - 1, curr_node)

            # backtracking
            board[r][c] = char

        # backtrack with every single cell
        for i in range(rows):
            for j in range(cols):
                backtrack(i, j, root)


        # return the results as a list
        return list(res)
