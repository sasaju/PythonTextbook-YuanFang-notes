# 使用正则表达式实现提取字符串中的数字 这样看起来就很简洁了
import re

message = "如果你1不知道啥是正则表达式那么你看看就好，考试不会考的6666ahhhaaa555.66a1.2221三个55a5"
message_yes = re.findall(r"\d+\.\d+|\d+", message)  # 使用正则表达式进行过滤
print(message_yes)
"""
实际运行的语句只有四行 但是如果不理解正则表达式看看就好，我们应该不会考的。
正则表达式在python中可以用来分析爬虫爬到的数据
"""
"""
还有一点问题就是可以使用python的filter函数结合lambda表达式把数字过滤出来
但是有一个严重的问题 就是输出结果全都是分开的单个数字无法分离
或许filter()有类似正则表达式中的贪婪模式我不知道
如果哪个大佬有办法用filter()实现了 请务必告诉我 谢谢
"""