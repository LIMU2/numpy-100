# pandas数据结构 data frame
#  相关性 协方差

import pandas as pd
import numpy as np
import pandas_datareader.data as web

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
print(df)
print(df.sum())

# axis 归约轴 0为行向，1为列向
print(df.sum(axis=1))  # Na被自动排除，可以通过禁用skipna来实现不排除na值

all_data = {ticker: web.get_data_yahoo(ticker) for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}
price = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})
volume = pd.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})
returns = price.pct_change()
price.corr()