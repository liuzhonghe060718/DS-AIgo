from collections import deque



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
def level_order(root):
    queue=deque([root])
    ans=[]
    while queue:
        now_node=queue.popleft()
        ans.append(now_node.val)
        if now_node.left:
            queue.append(now_node.left)
        if now_node.right:
            queue.append(now_node.right)
    return ''.join(ans)
n=int(input())
for _ in range(n):
    inorder_list=list(input())
    postorder_list=list(input())
    root0=buildTree(inorder_list,postorder_list)
    print(level_order(root0))
