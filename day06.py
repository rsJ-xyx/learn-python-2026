# day06.py —— W1 / D6
# 主题：周测（闭卷）
#
# 规则：不许看 day01~day05、不许问 AI、不许搜。
# 卡住超过 10 分钟就先跳过，最后再回来。
# 写完再对照答案反思——测的是"离开资料还能不能写"，不是分数。
#
#   python day06.py


print("=== day06: 第一周闭卷周测 ===")

# ---------------------------------------------------------------- Q1（15 分）
# 读 sample.txt，打印出现次数最多的 10 个单词及其次数
# 要求：忽略大小写，去掉标点，输出对齐
# TODO
def read_file(file):
    with open(file,"r",encoding="UTF-8") as f:
        content = f.read()
    return content

def clean(content,top):
    frequency = {}
    clean_content = content.lower()
    clean_char = [',', '.', '!', '?', ';', ':', '"', "'"]
    for char in clean_char:
        clean_content = clean_content.replace(char,"")
    sorted_word = clean_content.split()
    for word in sorted_word:
        frequency[word] = frequency.get(word,0)+1
    sorted_frequency = sorted(frequency.items(), key=lambda x:x[1],reverse=True)[:top]
    return sorted_frequency

def print_frequency(frequency):
    for word in frequency:
        print(f"{word[0]: <8}{word[1]: >4}")

def read_and_print(file,top):
    content = read_file(file)
    frequency = clean(content,top)
    print_frequency(frequency)
read_and_print("sample.txt",10)


# ---------------------------------------------------------------- Q2（10 分）
# 不排序整个列表（用 sorted），找出 [8, 3, 9, 9, 4] 里第二大的数
# 提示：可以先想清楚"最大值重复怎么办"
# TODO
def find_second_max(nums):
    second=largest = 0
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif second<num<largest:
            second = num
    return second
nums = [8, 3, 9, 9, 4]
the_second = find_second_max(nums)
print(f"第二大的数是{the_second}")
# ---------------------------------------------------------------- Q3（10 分）
# 判断 "A man, a plan, a canal: Panama" 是不是回文
# 要求：忽略大小写、忽略标点和空格
# TODO
def is_re(sentence):

    clean_sentence = sentence.replace(":","").replace(",","").replace(" ","").lower()
    return f"是否是回文,{clean_sentence == clean_sentence[::-1]}"

the_sentence = "A man, a plan, a canal: Panama"
print(is_re(the_sentence))


# ---------------------------------------------------------------- Q4（15 分）
# 两数之和：nums = [2, 7, 11, 15], target = 9，返回两个下标
# 先用两层循环写出来，再想能不能只遍历一次（用 dict 存"还差多少"）
# TODO
def sum_of_numbers(nums,target):
    result = []
    for index,num in enumerate(nums):
        for index2,num2 in enumerate(nums):
            if num+num2 == target and [index2,index] not in result:
                    result.append([index,index2])
    return result
nums = [2, 7, 11, 15]
target = 9
print(sum_of_numbers(nums,target))

# ---------------------------------------------------------------- Q5（15 分）
# 把 "  the  quick brown  fox " 处理成 "fox brown quick the"
# 要求：反转单词顺序，单词内部不变，去掉多余空格
# 提示：split() 不带参数会自动处理连续空格
# TODO
def flip_string(given_string):
    clean_string = given_string.split()
    flipped_string = clean_string[::-1]
    return " ".join(flipped_string)
flipped = flip_string("  the  quick brown  fox ")
print(flipped)


# ---------------------------------------------------------------- Q6（15 分）
# 写函数 count_words(text) -> dict，把你 Q1 里"清洗 + 统计"的部分抽出来
# 要求：函数没有 print，测试两个不同输入
# TODO
def count_words(text) -> dict:
    top = 5
    frequency = clean(text,top)
    dict_frequency = dict(frequency)
    return dict_frequency
print(count_words(the_sentence))
print(count_words("hello, nice to meet you, i am a new python learner"))

# ---------------------------------------------------------------- Q7（20 分，写文字，不写代码）
# 在下面三引号里写：这周你踩过的 3 个坑，每个坑写"现象 + 原因 + 以后怎么避免"
# 这一题的分量比前面所有代码都重——面试时讲的就是这些。
"""
1.题目要求没看清，如有时候要求打印结果我没写print，有时要求输出中文字符，我输成英文字符， 原因：审题时间不够，下笔仓促 解决方法：写完代码输出结果后再对比题目要求
2.split("")只能分割一个空格,而split()能分割连续空格。原因：python语法不熟悉，技术问题。解决方法：慢慢学习语法,反复试错。
3.对一些函数输出的结果类型不清楚，如dict.items()，这个函数输出的是视图对象。原因：对python语法不熟悉。 解决方法：dict.items()像是开了一扇窗观察字典,动态随字典变化，可用于迭代，如in,len()。
"""


print("=== 交卷：git add . && git commit -m 'day06: 第一周周测' ===")
