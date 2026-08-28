class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        # helper for dfs
        def dfs(node, index):
            # base case: index reach the end of the word
            if index == len(word):
                return node.is_end
            
            # current char of word
            char = word[index]

            # handle the wildchar: '.'
            if char == '.':
                # iterate thru each child node of children set
                for child in node.children.values():
                    # if can find the pattern to continue the word --> true
                    if dfs(child, index + 1):
                        return True
                return False
            
            else:
                if char not in node.children:
                    return False
                else:
                    return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)

