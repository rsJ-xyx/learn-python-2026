# day10.py —— W2 / D3
# 主题：哈希表
#
# 今天手写一个 dict。你会发现它只做两件事：
#   1. 把 key 变成一个下标（哈希函数）
#   2. 冲突了就挂在这个下标后面（链地址法）
#
# 写完你就明白：为什么 dict 查找是 O(1)、什么情况下会退化成 O(n)、
# 为什么 key 必须是"可哈希"的类型（list 不行，因为它能变）。
#
#   python day10.py


# ---------------------------------------------------------------- Q1
# 写一个最简单的哈希函数：把字符串所有字符的 ord 加起来，再对 size 取余。
#   hash_str("abc", 10) → (97+98+99) % 10 = 4
# 注意：这只是玩具，真实哈希函数要保证分布均匀。
# TODO
def hash_str(s, size):
    raise NotImplementedError


# ---------------------------------------------------------------- Q2
# 实现 HashMap（骨架已给），用**链地址法**处理冲突：
#   put(key, value)   已存在就覆盖
#   get(key)          不存在抛 KeyError(key)
#   delete(key)       删掉返回 True，不存在返回 False
#   __len__           当前元素个数
#   __contains__      让 `key in h` 能用
#
# 结构：self.buckets = [[], [], ...]，每个桶是一个列表，里面放 [key, value]。
# 同一个桶里可能有多对，查找时要遍历桶内的列表比较 key。
# TODO
class HashMap:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    def _index(self, key):
        """算出 key 应该落在哪个桶。O(1)"""
        return hash_str(str(key), self.capacity)

    def put(self, key, value):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def delete(self, key):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __contains__(self, key):
        raise NotImplementedError


# ---------------------------------------------------------------- Q3
# 加扩容：当 size / capacity > 0.75 时，把容量翻倍，并把所有元素重新放进去。
#
# 注意：扩容后每个元素的下标会变（因为除数变了），必须**重新计算**再插入。
# 在 put 里判断，扩容完再插。写一个 _resize() 方法。
# TODO


# ---------------------------------------------------------------- Q4
# 用随机数据压测：插入 1000 个随机 key，检查
#   ① len() == 1000
#   ② 每个 key 都能 get 到正确的值
#   ③ 期间至少发生过一次扩容（capacity 变大）
# 随机 key 用 f"key{i}" 或者 random.randint 都行。
# 这段写在下面的自测区里，不算新函数。
# TODO


# ---------------------------------------------------------------- Q5（思考题，只写注释）
# 为什么 dict 的 key 不能是 list，但可以是 tuple？
# 提示：跟"可哈希"有关，而可哈希的前提是"不可变"。
# TODO


# ================================================================ 自测
if __name__ == "__main__":
    assert hash_str("abc", 10) == 4

    h = HashMap()
    h.put("a", 1)
    assert h.get("a") == 1
    h.put("a", 2)
    assert h.get("a") == 2, "同 key 应覆盖"
    assert len(h) == 1, "覆盖不应增加长度"

    assert h.delete("a") is True
    assert h.delete("a") is False
    assert len(h) == 0

    try:
        h.get("不存在")
        raise AssertionError("取不存在的 key 应抛 KeyError")
    except KeyError:
        pass

    big = HashMap()
    for i in range(1000):
        big.put(f"key{i}", i)
    assert len(big) == 1000, "压测数量不对"
    for i in range(1000):
        assert big.get(f"key{i}") == i, f"key{i} 取回的值不对"
    assert big.capacity > 8, "应该发生过扩容"
    assert "key500" in big

    print("== day10 全部通过 ==")


print("=== 收工：git add . && git commit -m 'day10: 手写哈希表' ===")
