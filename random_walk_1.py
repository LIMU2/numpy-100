import random
import matplotlib.pyplot as plt
import numpy as np

# 简单随机漫步
position = 0
path = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    path.append(position)
img = plt.plot(path[:100])  # 对前100步可视化
plt.show()

# 抛硬币
nSteps = 1000
draws = np.random.randint(0, 2, size=nSteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()