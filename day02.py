# day02.py —— W1 / D2
# 主题：list / dict / set 的增删改查
#
# 这周的重点不是"记住方法名"，是养成一个习惯：
# 忘了就查，查完立刻用一次。写错比背下来重要。
#
#   python day02.py
from operator import index

print("=== day02: list / dict / set ===")

# ---------------------------------------------------------------- Q1
# 有一个列表 nums = [10, 20, 30, 40, 50, 60]
# 分别打印：前 3 个、后 3 个、整个列表倒序
# 提示：切片 nums[:3]  /  nums[-3:]  /  nums[::-1]
# TODO
nums = [10, 20, 30, 40, 50, 60]
print(nums[:3],nums[-3:],nums[::-1])

# ---------------------------------------------------------------- Q2
# 从空列表开始，依次做：
#   追加 3 个元素 → 在第 2 个位置插入一个 → 删掉第一个 → 弹出最后一个
# 每做一步打印一次列表，看清它的变化
# 提示：append / insert / pop / remove
# TODO
list1 = list()
list1.append(1)
print(list1)
list1.append(2)
print(list1)
list1.append(3)
print(list1)
list1.insert(1,4)
print(list1)
del list1[0]
print(list1)
list1.pop(-1)
print(list1)


# ---------------------------------------------------------------- Q3
# 用列表推导式，一行生成 1~20 中所有偶数的平方，打印结果
# 期望：[4, 16, 36, ...]
# TODO
list2 = [n**2 for n in range(1,21) if n % 2 == 0 ]
print(list2)

# ---------------------------------------------------------------- Q4
# 有两个列表：names = ["张三", "李四", "王五"]，scores = [88, 92, 75]
# 用 zip 把它们拼成一个字典 {"张三": 88, ...}，打印
# TODO
names = ["张三", "李四", "王五"]
scores = [88, 92, 75]
zipped = zip(names,scores)
dict1 = dict(zipped)
print(dict1)

# ---------------------------------------------------------------- Q5
# 遍历 Q4 的字典，打印成 "张三: 88 分"，并算出平均分
# 提示：for name, score in d.items():
# TODO
total_score = 0
for name,score in dict1.items():
    print(f"{name}:{score}分")
    total_score += score
print(total_score/len(dict1))



# ---------------------------------------------------------------- Q6
# 有重复的列表 data = [1, 2, 2, 3, 3, 3, 4]
# 1) 用 set 去重并打印
# 2) 两个集合 a = {1,2,3} b = {2,3,4}，打印交集、并集、差集
# TODO
data = [1, 2, 2, 3, 3, 3, 4]
set1 = set(data)
print(set1)
a = {1,2,3}
b = {2,3,4}
print(a&b)
print(a|b)
print(a-b)
print(b-a)



# ---------------------------------------------------------------- Q7
# 嵌套结构：students = {"张三": {"语文": 88, "数学": 92}, "李四": {"语文": 75, "数学": 60}}
# 打印每个人的总分，再打印每门课的平均分
# TODO
students = {"张三": {"语文": 88, "数学": 92}, "李四": {"语文": 75, "数学": 60}}
chinese = 0
math = 0
for name,grade in students.items():
    print(f"{name}:{sum(grade.values())}")
    chinese += grade['语文']
    math += grade['数学']
print(f"语文平均分:",chinese/len(students))
print(f"数学平均分:",math/len(students))

# ---------------------------------------------------------------- Q8
# 把 Q7 的结果按总分从高到低排序，打印成 "第1名 张三 180"
# 提示：sorted(students.items(), key=lambda x: ..., reverse=True)
# TODO
sorted_student = sorted(students.items(),key=lambda x: sum(x[1].values()),reverse=True)
for index,(name,grade) in enumerate(sorted_student,start=1):
    print(f"第{index}名 {name} {sum(grade.values())}")




print("=== 收工：今天写了几题？git add . 然后 commit ===")
