# day03.py —— W1 / D3
# 主题：分支与循环
#
# 今天的题都"看起来像作业题"，但它们练的是所有程序的基本骨架：
# 判断、循环、边界。以后写 Agent 的循环、重试、熔断，全是这些。
#
#   python day03.py
import math

print("=== day03: 分支与循环 ===")

# ---------------------------------------------------------------- Q1
# 打印九九乘法表（下三角，共 9 行）
# 提示：两层 for，内层 range(1, i+1)，用 end="" 控制不换行
# TODO
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end=" ")
    print()


# ---------------------------------------------------------------- Q2
# 打印 1~100 之间的所有素数
# 提示：写个内层循环判断能不能被 2~n-1 整除；先能跑，再想优化
# TODO
for i in range(1,101):
    if i == 1:
        continue
    for j in range(2,int(math.isqrt(i))+1):
        if i%j==0:
            break
    else:
        print(i,end=" ")



# ---------------------------------------------------------------- Q3
# 打印一个 5 行的金字塔：
#     *
#    ***
#   *****
# 提示：每行 = 空格 * (n-i) + 星号 * (2i-1)
# TODO
for i in range(1,6):
    print(f" " * (5-i),end="")
    print("*" *(2*i-1))


# ---------------------------------------------------------------- Q4
# FizzBuzz：1~30，能被 3 整除打印 Fizz，能被 5 整除打印 Buzz，
# 能被 15 整除打印 FizzBuzz，其余打印数字
# 注意：判断顺序很重要，想想为什么
# TODO
for i in range(1,31):
    if i%15==0:
        print("FizzBuzz",end=" ")
    elif i%5==0:
        print("Buzz",end=" ")
    elif i%3==0:
        print("Fizz",end=" ")
    else:
        print(i,end=" ")
print()


# ---------------------------------------------------------------- Q5
# 猜数字：程序随机 1~100 的整数，用 while 循环让用户一直猜，
# 提示"大了/小了"，猜对时打印猜了几次
# 提示：import random; random.randint(1, 100)；input() 拿到的是字符串，要 int()
# TODO
import random
target = random.randint(1,100)
guesses = 0
while True:
    try:
        guess = int(input("请猜一个1~100之间的整数"))
    except ValueError:
        print("请猜一个1~100之间的整数")
        continue

    if not 1<=guess<=100:
        print("超出范围，请输入1~100之间的整数")
        continue

    guesses += 1

    if guess == target:
        print(f"猜对了，一共猜了{guesses}次")
        break
    elif guess > target:
        print("大了")
    else:
        print("小了")
print(f"猜对了，一共猜了{guesses}次")


# ---------------------------------------------------------------- Q6
# 用 for 和 while 各写一次：求 1~100 的奇数之和
# 两次结果必须相同（2500），用 print 对比验证
# TODO
sum1 = sum2 = 0
for i in range(1,101):
    if i % 2 != 0:
        sum1 += i
print(sum1)

count = 1
while count < 101:
    if count % 2 != 0:
        sum2 += count
    count += 1
print(sum2)
print("两次结果相同吗",sum1 == sum2)



# ---------------------------------------------------------------- Q7
# 判断闰年：能被 4 整除且不能被 100 整除，或者能被 400 整除
# 用 2024、1900、2000 三个年份各测一次
# TODO
year = [2024,1900,2000]
for num in year:
    if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
        print(f"{num}是闰年")
    else:
        print(f"{num}不是闰年")



# ---------------------------------------------------------------- Q8
# 用 for 循环 + break / continue 各写一个例子：
# 找到列表 [3, 7, 12, 8, 5] 里第一个大于 10 的数就停（break）
# 打印 1~10 里除了 3 的倍数以外的数（continue）
# TODO
numbers =[3, 7, 12, 8, 5]
for num in numbers:
    if num > 10:
        print(f"第一个大于10的数是{num}")
        break

for num in range(1,11):
    if num % 3 == 0:
        continue
    print(num)


print("=== 收工：今天写了几题？git add . 然后 commit ===")
