# pandas 处理缺失值
import pandas as pd
import numpy as np
from numpy import nan as NA

# 过滤缺失值
data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())
data = pd.DataFrame([[1., 6.5, 3], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()  # dropna在默认情况下会删除包含缺失值的行
print(cleaned)
print('------')
cleaned = data.dropna(how='all')  # 删除所有值均为NA的行
print(cleaned)
cleaned = data.dropna(axis=1, how='all')
print(cleaned)
df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print(df)
print(df.dropna(thresh=2))

# 补全缺失值
print(df.fillna({1: 0.5, 2: 0}))  # 返回一个新对象
print(df.fillna(0, inplace=True))  # 修改已经存在的对象
df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[:2, 1] = NA
df.iloc[:4, 2] = NA
# 插值
# method :
# {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}, 默认值 None;
# 在Series中使用方法填充空白（‘backfill’, ‘bfill’向前填充，‘pad’, ‘ffill’向后填充）
df.fillna(method='ffill', limit=2)  # limit用于前向或后向的最大填充范围
