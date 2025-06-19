class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # 左子树
        self.right = None  # 右子树
        self.height = 1    # 当前节点的高度（初始为1）
class AVL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root = self._insert(value, self.root)

    def _insert(self, value, node):
        if not node:
            return Node(value)

        # 标准BST插入
        if value < node.value:
            node.left = self._insert(value, node.left)
        else:
            node.right = self._insert(value, node.right)

        # 更新高度
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # 计算平衡因子（左高减右高）
        balance = self._get_balance(node)

        # 四种不平衡情况及对应旋转

        # LL（左左）失衡
        if balance > 1 and value < node.left.value:
            return self._rotate_right(node)

        # LR（左右）失衡
        if balance > 1 and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # RR（右右）失衡
        if balance < -1 and value > node.right.value:
            return self._rotate_left(node)

        # RL（右左）失衡
        if balance < -1 and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        # 旋转
        y.left = z
        z.right = T2

        # 更新高度
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # 旋转
        x.right = y
        y.left = T2

        # 更新高度
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x
