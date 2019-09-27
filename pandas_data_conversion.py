import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 删除重复值
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'], 'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)
print(data.duplicated())  # 反应的是每一行是否与前一行相同
print(data.drop_duplicates())
data['v1'] = range(7)
print(data)
print(data.drop_duplicates(['k1']))
print(data.drop_duplicates(['k2']))
print(data.drop_duplicates(['v1']))
print(data.drop_duplicates(['k1'], keep='last'))

# 使用函数或者映射进行数据转换
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami',
                              'honey ham', 'nova lox'], 'ounces': [4.0, 3.0, 12.0, 6.0, 7.5, 8.0, 3.0, 5.0, 6.0]})
# 映射
meat_to_animal = {'bacon': 'pig', 'pulled pork': 'pig', 'pastrami': 'cow', 'corned beef': 'cow', 'honey ham': 'pig',
                  'nova lox': 'salmon'}
# 大写转换为小写
lower_cased = data['food'].str.lower()
# 增加新的一列
data['animal'] = lower_cased.map(meat_to_animal)  # map是一种可以便捷执行按元素转换及其他清洗相关操作的方法
print(data)
# 也可以用一句话
data['animal'] = data['food'].map(lambda x: meat_to_animal[x.lower()])

# 替代值
data = pd.Series([1., -999, 2., -999, 3., 10000])
print(data.replace(-999, np.nan))  # 不会替代原来的data，而是生成新的series)
print(data.replace([-999, 10000], [np.nan, 0]))
print(data.replace({-999: np.nan, 10000: 0}))

# 离散化和分箱
# 默认左开右闭
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)
# 对pandas.cut的结果中的箱数量的计数
print(pd.value_counts(cats))

# 频次分布图
data = np.random.randn(1000)
plt.hist(data, bins=50)
cats = pd.cut(data, bins=50)
print(pd.value_counts(cats))
# 折线图
y = pd.value_counts(cats).sort_index().values
# 拿到每个bin的中值
interval = cats.categories
MID = interval.mid
plt.plot(MID, y)
plt.show()
cats = pd.qcut(data, 4)  # 切成四份，由于qcut基于样本分位数进行分箱，这样可以得到等长的箱
