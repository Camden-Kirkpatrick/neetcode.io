class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_node(root, data):
    if not root:
        return TreeNode(data)
    
    if data > root.data:
        root.right = insert_node(root.right, data)
    elif data < root.data:
        root.left = insert_node(root.left, data)

    return root


def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.data)
    inorder(root.right)


def preorder(root):
    if not root:
        return
    
    print(root.data)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if not root:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.data)


#       4
#     /   \
#    3     6
#   /     / \
#  2     5   7
if __name__ == "__main__":
    root = TreeNode(4)
    insert_node(root, 3)
    insert_node(root, 6)
    insert_node(root, 2)
    insert_node(root, 5)
    insert_node(root, 7)

    print("inorder traversal:")
    inorder(root)
    print()

    print("preorder traversal:")
    preorder(root)
    print()

    print("postorder traversal:")
    postorder(root)
    print()