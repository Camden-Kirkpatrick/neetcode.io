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

#         10
#       /    \
#     8        13
#   /   \     /   \
# 4       9  11    17
if __name__ == "__main__":
    root = TreeNode(10)

    n1 = TreeNode(8)
    root.left = n1

    n2 = TreeNode(13)
    root.right = n2

    n3 = TreeNode(4)
    n1.left = n3

    n4 = TreeNode(11)
    n2.left = n4

    n5 = TreeNode(9)
    n1.right = n5

    n6 = TreeNode(17)
    n2.right = n6


    new_node = 12
    insert_node(root, new_node)
    print("Inserted", new_node)

    # Final Binary Tree
    #         10
    #       /    \
    #     8        13
    #   /   \     /   \
    # 4       9  11    17
    #               \
    #                12