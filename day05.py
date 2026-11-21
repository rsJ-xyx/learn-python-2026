# day05.py —— W1 / D5
# 主题：综合练习 —— 文本词频统计
#
# 今天的题合起来就是一个小工具：读文件 → 清洗 → 统计 → 排序 → 输出。
# 这套流程你以后会在"文档解析"里再见一次（RAG 的第一步）。
#
# 准备：在同目录新建 sample.txt，随便粘一段英文文章进去（几百词）。
#
#   python day05.py
import json
import argparse
from asyncio.windows_events import NULL

print("=== day05: 文本词频统计 ===")

# ---------------------------------------------------------------- Q1
# 读取 sample.txt 全部内容，打印字符数、单词数、行数
# 提示：open(file, encoding="utf-8") + .read()；单词数用 .split()
# TODO
def print_sample(sample):
    with open(sample,"r",encoding= 'UTF-8') as f:
        content = f.read()
        char_num = len(content)
        word_num = len(content.split())
        row_num = len(content.splitlines())
        print(f"字符数:{char_num},单词数:{word_num},行数:{row_num}")

# ---------------------------------------------------------------- Q2
# 清洗文本：全部转小写，把标点 , . ! ? ; : " ' 换成空格
# 提示：可以用 str.translate 或循环 replace；简单点用 replace 连着写
# TODO
def clean_sample(sample):
    try:
        with open(sample,"r",encoding= 'UTF-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("没有找到该文件")
        return NULL
    clean_char = [',', '.','!','?',';',':','"',"'"]
    clean_content = content.lower()
    for i in clean_char:
        clean_content = clean_content.replace(i," ")
    return clean_content

# ---------------------------------------------------------------- Q3
# 统计每个单词出现次数，返回一个 dict；打印出现次数最多的前 10 个
# 提示：counts[word] = counts.get(word, 0) + 1；排序用 sorted(counts.items(), key=..., reverse=True)[:10]
# TODO
def statistic_function(clean_content,top):
    frequency = {}
    for word in clean_content.split():
        frequency[word] = frequency.get(word,0)+1
    sort_dict_top = dict(sorted(frequency.items(), key=lambda x:x[1],reverse=True)[:top])
    return sort_dict_top


# ---------------------------------------------------------------- Q4
# 排序稳定性实验：
# words = [("apple", 3), ("banana", 1), ("cherry", 3), ("date", 1)]
# 先按次数降序，次数相同的按字母升序。打印结果
# 提示：sorted(words, key=lambda x: (-x[1], x[0]))
# TODO
def experiment(words):
    sort_words = sorted(words,key=lambda x:(-x[1],x[0]))
    print(sort_words)



# ---------------------------------------------------------------- Q5
# 美化输出：打印成对齐的两列，形如
#   apple      12
#   banana      9
# 提示：f"{word:<12}{count:>4}"，< 左对齐 > 右对齐，数字是宽度
# TODO
def beautify_print(content):
    for word in content.items():
        print(f"{word[0]:<12}{word[1]:>4}")


# ---------------------------------------------------------------- Q6
# 把 Top10 结果存成 JSON 文件 top10.json，再读回来看是否一致
# 提示：import json; json.dump(..., ensure_ascii=False, indent=2)
# TODO
def save_and_read(sort_dict):
    try:
        with open("top.json","w",encoding="UTF-8") as f:
            json.dump(sort_dict,f,ensure_ascii=False,indent=2)
    except FileNotFoundError:
        print("没有找到改文件")
        return NULL
    try:
        with open("top.json","r",encoding="UTF-8") as f:
            json_reader = json.load(f)
        print(json_reader)
        print(f"是否相等:{json_reader == sort_dict}")
    except FileNotFoundError:
        print("没有找到该文件")
        return NULL
# ---------------------------------------------------------------- Q7
# 用 argparse 让文件名可以从命令行传：
#   python day05.py --file sample.txt --top 5
# 提示：parser.add_argument("--file", default="sample.txt")
# TODO
def main():
    parser = argparse.ArgumentParser(description='文件单词频率统计脚本')
    parser.add_argument("--file",type=str, default="sample.txt")
    parser.add_argument("--top",type=int, default=10)
    args = parser.parse_args()
    print_sample(args.file)
    clean_content = clean_sample(args.file)
    sort_dict = statistic_function(clean_content,args.top)
    beautify_print(sort_dict)
    experiment( [("apple", 3), ("banana", 1), ("cherry", 3), ("date", 1)])
    save_and_read(sort_dict)

if __name__ == "__main__":
    main()

print("=== 收工：今天写了几题？git add . 然后 commit ===")
