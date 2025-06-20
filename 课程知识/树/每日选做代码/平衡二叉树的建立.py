class TreeNode:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

def get_height(node):
    return node.height if node else 0

def update_height(node):
    node.height = max(get_height(node.left), get_height(node.right)) + 1

def get_balance_factor(node):
    return get_height(node.left) - get_height(node.right)

def left_rotate(node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node
    update_height(node)
    update_height(new_root)
    return new_root

def right_rotate(node):
    new_root = node.left
    node.left = new_root.right
    new_root.right = node
    update_height(node)
    update_height(new_root)
    return new_root

def insert(root, data):
    if not root:
        return TreeNode(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    update_height(root)
    balance_factor = get_balance_factor(root)
    if balance_factor > 1:
        if get_balance_factor(root.left) < 0:
            root.left = left_rotate(root.left)
        root = right_rotate(root)
    elif balance_factor < -1:
        if get_balance_factor(root.right) > 0:
            root.right = right_rotate(root.right)
        root = left_rotate(root)
    return root

def pre_order_traversal(root, result):
    if not root:
        return
    result.append(root.data)
    pre_order_traversal(root.left, result)
    pre_order_traversal(root.right, result)

def main():
    n = int(input())
    nodes = list(map(int, input().split()))
    root = None
    for data in nodes:
        root = insert(root, data)
    result = []
    pre_order_traversal(root, result)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()