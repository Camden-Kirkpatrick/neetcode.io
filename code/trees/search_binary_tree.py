class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search_tree(root, target):
    if not root:
        return False
    
    if target > root.data:
        return search_tree(root.right, target)
    elif target < root.data:
        return search_tree(root.left, target)
    else:
        return True


if __name__ == "__main__":
    root = TreeNode(10)
    n1 = TreeNode(8)
    root.left = n1
    n2 = TreeNode(13)
    root.right = n2

    target = 13
    result = search_tree(root, target)
    print(f"{target} was {'found' if result else 'not found'}")

