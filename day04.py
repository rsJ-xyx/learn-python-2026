# day04.py —— W1 / D4
# 主题：函数、参数、返回值
#
# 今天的目标只有一个：把前三天写过的代码"拆成函数"。
# 会写函数，才算会写程序；不会拆函数，代码永远只能跑一次。
#
#   python day04.py
import math
print("=== day04: 函数 ===")

# ---------------------------------------------------------------- Q1
# 写 is_prime(n) -> bool，判断 n 是不是素数；再写一个函数打印 1~100 的素数
# 要求：函数里只做判断，打印放在调用处（职责分离）
# TODO
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def print_prime():
    for i in range(1,101):
        if is_prime(i):
            print(i)

print_prime()

# ---------------------------------------------------------------- Q2
# 写 greet(name, greeting="你好")，调用时：
#   greet("张三")            → 你好，张三
#   greet("李四", "早上好")   → 早上好，李四
#   greet(greeting="晚上好", name="王五")  → 关键字参数，顺序可以打乱
# TODO
def greet(name,greeting="你好"):
    print(f"{greeting}，{name}")

greet("张三")
greet("李四", "早上好")
greet(greeting="晚上好", name="王五")

# ---------------------------------------------------------------- Q3
# 写一个函数返回两个值：min_and_max(nums) -> (最小值, 最大值)
# 调用时用 a, b = min_and_max([3, 1, 9, 4]) 一次接住两个返回值
# TODO
def min_and_max(nums):
    min_num = min(nums)
    max_num = max(nums)
    return min_num, max_num

the_min,the_max = min_and_max([3, 1, 9, 4])
print(f"最小值是{the_min},最大值是{the_max}")


# ---------------------------------------------------------------- Q4
# 写 sum_all(*args) 接受任意个数字求和
# 写 print_info(**kwargs) 接受任意个"键=值"并逐行打印
# 提示：args 是元组，kwargs 是字典
# TODO
def sum_all(*args):
    total = 0
    for num in args:
        try:
            total += num
        except TypeError:
            print("发现非法输入,已跳过")
    return total

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print(sum_all(1,2,3,4,5,"苹果"))
print_info(chinese=88,math=90)


# ---------------------------------------------------------------- Q5
# 用递归写 factorial(n)（阶乘）和 fib(n)（斐波那契第 n 项）
# 注意：递归必须有终止条件，想想 fib 为什么算到 30 就很慢
# TODO
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))
print(factorial(5))

# ---------------------------------------------------------------- Q6
# 把 day02 的 Q7（学生成绩）重构成 3 个函数：
#   total_of(student)  → 某人总分
#   class_average(students, subject) → 某科平均分
#   rank(students)     → 按总分排序的列表
# 每个函数不超过 6 行
# TODO
Students = {"张三": {"语文": 88, "数学": 92}, "李四": {"语文": 75, "数学": 60}}
def total_of(score: dict[str, int]) -> int:
    """返回某个学生的总分。"""
    return sum(score.values())

def class_average(students:dict[str,dict[str,int]], subject:str)->float:
    """返回某科目的平均分。

       Args:
           students: 学生成绩表，形如 {"张三": {"语文": 88}}。
           subject: 科目名，必须是每个人成绩里都有的 key。

       Returns:
           平均分，保留完整精度。
       """
    result = 0
    for name, grades in students.items():
        result += grades[subject]
    return result/len(students)

def rank(students:dict[str,dict[str,int]])->list[tuple[str, int]]:
    """按总分从高到低排序，返回 [(姓名, 总分), ...]。"""
    total_grades={}
    for name, grades in students.items():
        total_grades[name] = sum(grades.values())
    sorted_students = sorted(total_grades.items(), key=lambda x:x[1], reverse=True)
    return sorted_students

print(total_of(Students["张三"]))
print(class_average(Students,"语文"))
print(class_average(Students,"数学"))
print(rank(Students))




# ---------------------------------------------------------------- Q7
# 给 Q6 的三个函数各加 docstring 和类型注解，例如：
#   def total_of(scores: dict[str, int]) -> int:
#       """返回某个学生的总分。"""
# 提示：PyCharm 里输入三个引号会自动生成模板
# TODO



print("=== 收工：今天写了几题？git add . 然后 commit ===")
