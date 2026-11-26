# day09.py —— W2 / D2
# 主题：栈与队列
#
# 昨天写了链表，今天用两种容器做两件事：
#   栈（Stack）：后进先出 LIFO  —— 括号匹配、撤销、函数调用
#   队列（Queue）：先进先出 FIFO —— 任务排队、BFS 遍历
#
# 这两个结构你以后天天见：Agent 的任务队列、消息队列都是队列，
# 递归和回溯都是栈。今天写一遍，以后见到不会发怵。
#
#   python day09.py


from day08 import Node


# ---------------------------------------------------------------- Q1
# 用 list 实现 Stack：push / pop / peek / is_empty / __len__
# pop 在空栈上要抛 IndexError("栈是空的")，不能返回 None 蒙混过去
# TODO
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        """入栈。O(1)"""
        self.items.append(value)

    def pop(self):
        """出栈并返回。O(1)"""
        return self.items.pop()

    def peek(self):
        """看一眼栈顶但不弹出。O(1)"""
        return self.items[-1]

    def is_empty(self):
        return not self.items

    def __len__(self):
        return len(self.items)

# ---------------------------------------------------------------- Q2
# 用你写的 Stack 判断括号是否匹配：()[]{} 三种括号
# 返回 True / False
#   "{[()]}"  → True
#   "([)]"    → False
#   "(("      → False
# 提示：左括号入栈；遇到右括号看栈顶是不是对应的左括号，不是就 False；
#       扫完后栈必须为空。
# TODO
def is_balanced(text):
    stack = Stack()
    pairs = {")":"(","}":"{","]":"["}
    for char in text:
        if char in "(,{,[":
            stack.push(char)
        elif char in pairs:
            if stack.is_empty() or pairs[char] != stack.peek():
                return False
            stack.pop()
    return stack.is_empty()

# ---------------------------------------------------------------- Q3
# 用两个栈实现一个队列（经典的"栈实现队列"）：
#   in_stack  负责 push
#   out_stack 负责 pop：out 空了就把 in 全部倒过来
# 要求 push / pop 均摊 O(1)
# TODO
class QueueByStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, value):
        self.in_stack.append(value)

    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()



    def is_empty(self):
        if not self.out_stack and not self.in_stack:
            return True
        else:
            return False


# ---------------------------------------------------------------- Q4
# 用**链表**实现队列，enqueue / dequeue 都必须是 O(1)。
# 关键：同时保存 head 和 tail 两个指针，出队改 head，入队改 tail。
# 注意空队列出队要抛 IndexError。
# TODO
class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)
        self.size += 1
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    def dequeue(self):
        if self.head is None:
            raise IndexError("队列为空")
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return node.value

    def __len__(self):
        return self.size


# ---------------------------------------------------------------- Q5
# 用 collections.deque 模拟一个"打印任务队列"：
#   不断加入任务，每次取最早的那个打印，打印 3 个就停。
# 再把 deque 换成 list 试一次，感受 pop(0) 和 popleft() 的差别。
# 只写注释说明差别即可（不用真跑两遍）。
# TODO


# ================================================================ 自测
if __name__ == "__main__":
    s = Stack()
    assert s.is_empty() is True
    s.push(1); s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert len(s) == 1
    try:
        Stack().pop()
        raise AssertionError("空栈 pop 应该抛 IndexError")
    except IndexError:
        pass

    assert is_balanced("{[()]}") is True
    assert is_balanced("([)]") is False
    assert is_balanced("((") is False
    assert is_balanced("") is True

    q = QueueByStacks()
    for i in [1, 2, 3]:
        q.push(i)
    assert q.pop() == 1, "队列应该先进先出"
    q.push(4)
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.is_empty() is True

    lq = LinkedQueue()
    for i in [1, 2, 3]:
        lq.enqueue(i)
    assert lq.dequeue() == 1
    assert len(lq) == 2
    assert lq.dequeue() == 2
    assert lq.dequeue() == 3
    try:
        lq.dequeue()
        raise AssertionError("空队列应抛 IndexError")
    except IndexError:
        pass

    print("== day09 全部通过 ==")
    print("=== 收工：git add . && git commit -m 'day09: 栈与队列' ===")


