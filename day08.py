# day08.py —— W2 / D1
# 主题：类与单链表
#
# 这一周开始写"数据结构"：用类把数据和操作打包在一起。
# 目的不是造轮子，是**知道轮子怎么转**——面试官问"链表和数组有什么区别"，
# 你得能说出"为什么",而不是背结论。
#
# 类的最小知识（今天够用）：
#   class Foo:
#       def __init__(self, x):    # 构造方法，创建对象时自动调用
#           self.x = x            # self 就是"这个对象自己"
#       def bar(self):            # 方法，第一个参数永远是 self
#           return self.x
#   f = Foo(1)
#   print(f.bar())
#
# 今天的规矩：所有方法都用 docstring 写上复杂度，例如 """尾部追加。O(n)"""
#
#   python day08.py


# ---------------------------------------------------------------- Q1
# 写 Node 类：保存 value 和下一个节点的引用 next（默认 None）
# 再写 __repr__，让它打印出来是 Node(3) 这种形式
# TODO
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"


# ---------------------------------------------------------------- Q2
# 写 LinkedList 类（骨架已给），实现四个方法：
#   append(value)   尾部追加          —— 复杂度？
#   __len__()       返回节点数，让 len(ll) 能用
#   __iter__()      让它能被 for 遍历
#   to_list()       转成普通列表，方便打印和断言
#
# 提示：append 有两种写法——每次都从头走到尾（O(n)），
#       或者额外维护一个 self.tail（O(1)）。先写 O(n) 版，通了再改。
# TODO
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        """尾部追加。O(n)"""
        node = Node(value)
        self.size += 1

        if self.head is None:
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node



    def __len__(self):
        return self.size


    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next


    def to_list(self):
        return list(self)

    def insert(self,index,value):
        node = Node(value)
        self.size += 1
        if self.head is None or index == 0:
            node.next = self.head
            self.head = node
            return

        cur = self.head
        for i in range(index-1):
            if cur.next is None:
                break
            cur = cur.next

        node.next = cur.next
        cur.next = node

    def delete(self,value):
        if self.head is None:
            return False
        cur = self.head
        prev = None
        while cur is not None:
            if cur.value == value:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                self.size -= 1
                return True
            prev = cur
            cur = cur.next
        return False

    def reverse(self):
        if self.head is None or self.head.next is None:
            return
        prev = None
        cur = self.head
        nxt = cur.next
        while nxt is not None:
            cur.next = prev
            prev = cur
            cur = nxt
            nxt = cur.next
        cur.next = prev
        self.head = cur
# ---------------------------------------------------------------- Q3
# 给 LinkedList 加两个方法（直接在上面那个类里补）：
#   insert(index, value)   在下标 index 处插入（index 超范围就追加到尾部）
#   delete(value)          删除第一个值为 value 的节点，删掉返回 True，没找到返回 False
#
# 边界一定要处理：空链表、删头节点、删尾节点、index=0



# ---------------------------------------------------------------- Q4
# 给 LinkedList 加 reverse()：**原地**反转链表，不许转成 list 再倒过来。
# 要求 O(n) 时间、O(1) 额外空间（只许用几个指针变量）。
#
# 提示：三个指针 prev / cur / nxt，边遍历边改 next 指向。
#       画一遍图再写，比直接敲快。



# ---------------------------------------------------------------- Q5（思考题，只写注释）
# 同样是"在中间插入一个元素"：
#   list.insert(0, x)          → O(n)，因为后面所有元素都要后移
#   链表 insert(0, x)          → O(1)，只改一个指针
# 那为什么现实中到处都在用 list，而不是链表？写三行你的理解。
# 现实里 list 用得多，原因：
# 1. 缓存局部性：数组连续存放，遍历时 CPU 缓存命中率高；链表指针跳跃，频繁 cache miss
# 2. 每个节点有指针+分配开销，内存占用高
# 3. 链表的 O(1) 插入要求"已持有节点引用"；只有下标时找位置仍是 O(n)
# 4. 数组的搬移是 memmove，常数极小
# 链表仍用在：LRU 缓存（dict+双向链表）、内核 list_head、free list、持久化数据结构


# ================================================================ 自测
# 跑 `python day08.py`，看到"全部通过"才算今天做完。
# 报错信息里会告诉你是哪一条断言失败。
if __name__ == "__main__":
    assert Node(3).value == 3
    assert repr(Node(3)) == "Node(3)"

    ll = LinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    assert len(ll) == 3, "len() 不对"
    assert ll.to_list() == [1, 2, 3], "append 顺序不对"
    assert list(ll) == [1, 2, 3], "__iter__ 没实现好"
    ll.insert(0, 0)
    assert ll.to_list() == [0, 1, 2, 3], "insert(0) 不对"
    ll.insert(99, 4)
    assert ll.to_list() == [0, 1, 2, 3, 4], "insert 超范围应追加"

    assert ll.delete(2) is True
    assert ll.to_list() == [0, 1, 3, 4]
    assert ll.delete(999) is False, "删不存在的值应返回 False"
    assert ll.delete(0) is True, "删头节点"
    assert ll.to_list() == [1, 3, 4]

    ll.reverse()
    assert ll.to_list() == [4, 3, 1], "reverse 不对"

    empty = LinkedList()
    assert len(empty) == 0
    assert empty.to_list() == []

    print("== day08 全部通过 ==")


print("=== 收工：git add . && git commit -m 'day08: 单链表' ===")
