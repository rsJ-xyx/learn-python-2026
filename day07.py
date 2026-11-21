# day07.py —— W1 / D7
# 主题：复盘日（代码量最少，收获最大）
#
# 今天不学新东西，只做三件事：修、补、写。
# 周末复盘的价值，等于你这一周所有练习的总和。
#
#   python day07.py

import argparse
from day05 import print_sample, clean_sample, statistic_function, beautify_print, save_and_read

print("=== day07: 第一周复盘 ===")

# ---------------------------------------------------------------- Q1
# 重写本周你认为最难的那一题——不看之前的代码，从空白开始写一遍。
# 写完对比两版，把"这次为什么更快/还是卡住"写在下面的注释里。
# TODO
parser = argparse.ArgumentParser(description="文本单词频率统计器")
parser.add_argument("--file",type=str,default='sample.txt')
parser.add_argument("--top",type=int,default=10)
args = parser.parse_args()
print_sample(args.file)
clean_content = clean_sample(args.file)
sort_dict = statistic_function(clean_content,args.top)
beautify_print(sort_dict)
save_and_read(sort_dict)

"""这次写的速度快多了，因为上次是第一次接触parse这个东西，而且没有分函数写，导致后面改花了太多时间，这次利用现有函数，几分钟搞定"""
# ---------------------------------------------------------------- Q2
# 给 day01.py 所有的 input 和文件读写加上 try/except，
# 让它遇到"文件不存在""用户输入非数字"时不崩，而是给出提示。
# 提示：except FileNotFoundError: / except ValueError:
# TODO



# ---------------------------------------------------------------- Q3
# 整理《Python 坑点清单》：把本周所有报错抄下来，每条写"报错原文 + 一句话原因"。
# 至少 8 条。这份清单以后每次写错都往里加，是你最私人的教材。
# 直接写在这个文件里，用三引号包起来。
"""
1. IndentationError: unexpected indent —— 缩进错，Python 靠缩进分代码块
2.
3.
"""




# ---------------------------------------------------------------- Q4
# 把 README.md 的进度表更新成 W1 完成，并加一段"本周学到什么"（3 行就够）
# TODO
"""
1.python数据基本类型
2.切片相关法则
3.构造函数
"""


# ---------------------------------------------------------------- Q5
# 给下周的自己留 3 句话：你现在最不确定的是什么？
"""
1.现在学的怎么用到agent中
2.为什么学ai用的语言是python不是其他java,c之类的
3.python最难的地方在哪
"""





print("=== 收工：commit 一次，第一周就结束了 ===")
