import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['16 (8)', '32 (16)', '64 (16)', '64 (48)', '64 (32)\n(Ours)']
upenn_gbm_r5 = [23.1, 23.2, 23.3, 23.7, 25.1]
upenn_gbm_r10 = [32.0, 32.1, 31.8, 32.1, 34.5]
endocrine_patient_data_r5 = [37.1, 36.1, 35.7, 36.7, 39.4]
endocrine_patient_data_r10 = [47.5, 47.6, 47.2, 47.7, 50.1]

# Set up the bar chart
x = np.arange(len(categories))
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

# Create bars
rects1 = ax.bar(x - 1.5*width, upenn_gbm_r5, width, label='UG R@5', color='#8884d8')
rects2 = ax.bar(x - 0.5*width, upenn_gbm_r10, width, label='UG R@10', color='#82ca9d')
rects3 = ax.bar(x + 0.5*width, endocrine_patient_data_r5, width, label="EPD R@5", color='#ffc658')
rects4 = ax.bar(x + 1.5*width, endocrine_patient_data_r10, width, label="EPD R@10", color='#ff7300')

# Customize the chart
ax.set_ylabel('Value')
ax.set_xlabel('K (K\')')
ax.set_title('Impact of the Number of Anchors')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# Add value labels on top of each bar
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

plt.tight_layout()
plt.savefig('columBar-figure.svg', format='svg', dpi=300)
plt.show()