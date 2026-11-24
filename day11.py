# day11.py —— W2 / D4
# 主题：二叉树与三种遍历
#
# 遍历是树的一切：查找、统计、序列化、判断，全都建立在遍历上。
# 今天递归和迭代各写一遍——**递归帮你理解，迭代帮你在面试里不慌**
# （面试官经常会说："递归写完了，用栈写一个。"）
#
# 树的表示：TreeNode(value, left, right)，空子树用 None。
#
#   python day11.py


# ---------------------------------------------------------------- Q1
# 写 TreeNode 类：value / left / right，默认都是 None
# TODO
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# ---------------------------------------------------------------- Q2
# 从"层序列表"建树：用 None 表示空位。
#   [1, 2, 3, 4, 5, None, 6]  表示
#           1
#        2     3
#      4   5     6
#
# 提示：用 collections.deque 当队列。根先入队；
#       每次弹出一个节点，依次从列表里取两个值当它的左右孩子，孩子非 None 就入队。
#       遇到 None 就跳过（占位，但不入队）。
# TODO
def build_tree(values):
    raise NotImplementedError


# ---------------------------------------------------------------- Q3
# 三种递归遍历，各自返回一个列表：
#   preorder   根 → 左 → 右
#   inorder    左 → 根 → 右
#   postorder  左 → 右 → 根
# TODO
def preorder(node):
    raise NotImplementedError


def inorder(node):
    raise NotImplementedError


def postorder(node):
    raise NotImplementedError


# ---------------------------------------------------------------- Q4
# 用**栈**（不许递归）重写前序和中序，体会"递归其实是用系统栈"。
# 前序最简单：根入栈，弹出就访问，然后右孩子先入栈、左孩子后入栈。
# 中序要想清楚：一路向左压栈，到底了再弹。
# TODO
def preorder_iter(node):
    raise NotImplementedError


def inorder_iter(node):
    raise NotImplementedError


# ---------------------------------------------------------------- Q5
# 层序遍历（BFS）：用队列，一层一层地输出，返回 [1, 2, 3, 4, 5, 6]
# 进阶（可选）：返回 [[1], [2, 3], [4, 5, 6]] 这种按层分组的形式
# TODO
def level_order(node):
    raise NotImplementedError


# ---------------------------------------------------------------- Q6
# 写三个小函数：
#   tree_height(node)  → 树高，空树返回 0
#   tree_size(node)    → 节点总数
#   find(node, value)  → 找到返回节点，找不到返回 None
# TODO


# ---------------------------------------------------------------- Q7
# 判断是不是二叉搜索树（BST）：左子树全部小于根，右子树全部大于根。
#
# 陷阱：只比较"父节点和左右孩子"是错的。下面这棵树不是 BST，但每个节点都满足局部条件：
#         5
#       3   8
#     1   6
#   6 在 5 的左子树里，比 5 大 → 违反 BST。
#
# 正解：中序遍历结果必须是严格递增的；或者递归时传上下界。
# TODO
def is_bst(node):
    raise NotImplementedError


# ================================================================ 自测
if __name__ == "__main__":
    root = build_tree([1, 2, 3, 4, 5, None, 6])
    assert root.value == 1 and root.left.value == 2 and root.right.value == 3

    assert preorder(root) == [1, 2, 4, 5, 3, 6], "前序不对"
    assert inorder(root) == [4, 2, 5, 1, 3, 6], "中序不对"
    assert postorder(root) == [4, 5, 2, 6, 3, 1], "后序不对"

    assert preorder_iter(root) == [1, 2, 4, 5, 3, 6], "迭代前序不对"
    assert inorder_iter(root) == [4, 2, 5, 1, 3, 6], "迭代中序不对"

    assert level_order(root) == [1, 2, 3, 4, 5, 6], "层序不对"
    assert tree_height(root) == 3
    assert tree_size(root) == 6
    assert find(root, 5) is not None
    assert find(root, 99) is None

    assert is_bst(build_tree([5, 3, 8, 1, 4, 7, 9])) is True
    assert is_bst(build_tree([5, 3, 8, 1, 6, 7, 9])) is False, "6 在左子树里，不是 BST"

    assert build_tree([]) is None
    assert tree_height(None) == 0

    print("== day11 全部通过 ==")


print("=== 收工：git add . && git commit -m 'day11: 二叉树遍历' ===")
