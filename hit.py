import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 构造数据表
data = {
    "K": [16, 32, 64, 64, 64],
    "K'": [8, 16, 16, 48, 32],
    "UG-R@5": [23.1, 23.2, 23.3, 23.7, 25.1],
    "UG-R@10": [32.0, 32.1, 31.8, 32.1, 34.5],
    "EPD-R@5'": [37.1, 36.1, 36.7, 36.7, 39.4],
    "EPD-R@10'": [47.5, 47.6, 47.2, 47.7, 50.1]
}

df = pd.DataFrame(data)

# 创建热力图的绘制
plt.figure(figsize=(10, 6))

# 使用 K 和 K' 作为坐标轴，R@5, R@10, R@5', R@10' 的值为颜色
sns.heatmap(df.set_index(['K', "K'"]), annot=True, cmap="Blues", linewidths=0.5, fmt=".1f")

plt.title("Heatmap of R@5, R@10, R@5', R@10' values across different K and K'")
plt.savefig('hit-figure.svg', format='svg', dpi=300)
plt.show()
