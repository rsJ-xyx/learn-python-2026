# day13.py —— W2 / D6
# 主题：JSON 持久化 + 异常处理 + 组装
#
# 今天把这一周写的东西"变成能用的东西"：数据存到硬盘，下次打开还在。
# 这是所有真实程序的共同点——**程序会退出，数据不能丢**。
#
#   python day13.py
#
# 今天的三个新东西：
#   1. json.dump / json.load   —— 结构 ↔ 文件
#   2. try/except 的三种具体异常 —— 文件不存在、内容坏了、字段缺失
#   3. 把散落的类挪进 data_structures.py，用 import 复用


import json
import os

CONTACTS_FILE = "contacts.json"


# ---------------------------------------------------------------- Q1
# 整理：把 day08 的 LinkedList、day10 的 HashMap 挪进一个新文件 data_structures.py，
# 然后在这里 `from data_structures import LinkedList` 试试能不能用。
#
# 注意：data_structures.py 里如果有顶层测试代码，import 时会被执行——
# 记得把它们包进 `if __name__ == "__main__":`。
#
# 这一步做完，你的仓库就有了第一个"模块"，而不是一堆脚本。
# TODO（写注释记录你挪了哪些、import 是否成功）


# ---------------------------------------------------------------- Q2
# 通讯录的数据长这样（先用普通 list[dict]，不依赖你自己写的类）：
#   [{"name": "张三", "phone": "13800000000", "email": "z@x.com"}, ...]
#
# 写 save_contacts(contacts, path=CONTACTS_FILE)：
#   把列表写进 JSON 文件，要求中文可读（ensure_ascii=False）、缩进 2、末尾换行。
# TODO
def save_contacts(contacts, path=CONTACTS_FILE):
    raise NotImplementedError


# ---------------------------------------------------------------- Q3
# 写 load_contacts(path=CONTACTS_FILE) -> list[dict]，要能扛住三种情况：
#   ① 文件不存在        → 返回空列表 []（首次运行很正常，不算错误）
#   ② 文件内容不是合法 JSON → 打印提示，返回 []
#   ③ 读到的不是列表      → 打印提示，返回 []
#
# 提示：FileNotFoundError / json.JSONDecodeError / isinstance(data, list)
# TODO
def load_contacts(path=CONTACTS_FILE):
    raise NotImplementedError


# ---------------------------------------------------------------- Q4
# 写一个命令行通讯录，功能：
#   1 添加   2 查看全部   3 按姓名查找   4 删除   5 退出
# 要求：
#   - 每次增删后立刻存盘
#   - 输入菜单时如果输的不是数字，提示重来，不能崩
#   - 姓名重复时提示"已存在"
# TODO
def run_cli():
    contacts = load_contacts()
    raise NotImplementedError


# ---------------------------------------------------------------- Q5（思考题，只写注释）
# 为什么 set 和自定义对象不能直接 json.dump？
# 提示：JSON 只认识 dict / list / str / int / float / bool / None 七种类型。
# 那自定义对象怎么办？（关键词：__dict__、dataclasses.asdict）
# TODO


# ================================================================ 自测
if __name__ == "__main__":
    import tempfile

    tmp = os.path.join(tempfile.gettempdir(), "test_contacts.json")
    if os.path.exists(tmp):
        os.remove(tmp)

    # ① 文件不存在 → 空列表
    assert load_contacts(tmp) == []

    # ② 正常存取
    data = [{"name": "张三", "phone": "138", "email": "z@x.com"}]
    save_contacts(data, tmp)
    assert load_contacts(tmp) == data

    # ③ 中文没被转义
    with open(tmp, encoding="utf-8") as f:
        assert "张三" in f.read(), "ensure_ascii=False 没加"

    # ④ 文件坏了 → 不崩，返回 []
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("{这不是合法 JSON")
    assert load_contacts(tmp) == []

    # ⑤ 内容不是列表 → 返回 []
    with open(tmp, "w", encoding="utf-8") as f:
        f.write('{"name": "张三"}')
    assert load_contacts(tmp) == []

    os.remove(tmp)
    print("== day13 全部通过 ==")


print("=== 收工：git add . && git commit -m 'day13: JSON 持久化与通讯录' ===")
