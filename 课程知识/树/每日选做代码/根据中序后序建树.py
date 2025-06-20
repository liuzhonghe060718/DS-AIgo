class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    # 后序遍历的最后⼀个元素是当前的根节点
    root_val = postorder.pop()
    root = TreeNode(root_val)
    # 在中序遍历中找到根节点的位置
    root_index = inorder.index(root_val)
    # 构建右⼦树和左⼦树
    root.right = buildTree(inorder[root_index + 1:], postorder)
    root.left = buildTree(inorder[:root_index], postorder)
    return root

def preorderTraversal(root):
    result = []

    if root:
        result.append(root.val)
        result.extend(preorderTraversal(root.left))
        result.extend(preorderTraversal(root.right))
    return result
# 读取输⼊
inorder = input().strip()
postorder = input().strip()
# 构建树
root = buildTree(list(inorder), list(postorder))
# 输出前序遍历序列
print(''.join(preorderTraversal(root)))