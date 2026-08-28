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
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end
            
            char = word[idx]

            if char == '.':
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True
                return False
            

            else:
                if char not in node.children:
                    return False
                else:
                    return dfs(node.children[char], idx + 1)
        
        return dfs(self.root, 0)