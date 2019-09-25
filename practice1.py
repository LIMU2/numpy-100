# practice：函数是个对象

# 引入正则表达式模块
import re


# 如下标点用空代替
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)


# 清晰的规则
# strip 移除前/后的空格
# title
#         More specifically, words start with uppercased characters and all remaining
#         cased characters have lower case.
clean_ops = [str.strip, remove_punctuation, str.title]


def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result


states = ['   Alabama ', ' #Geiorgia!', 'Georgia', 'georgia', 'FlorIda', 'south  carolina##', 'West virginia?']
print(clean_strings(states, clean_ops))