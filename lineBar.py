import matplotlib.pyplot as plt

# Data
x_labels = ['16 (8)', '32 (16)', '64 (16)', '64 (48)', '64 (32)\n(Ours)']
upenn_gbm_r5 = [23.1, 23.2, 23.3, 23.7, 25.1]
upenn_gbm_r10 = [32.0, 32.1, 31.8, 32.1, 34.5]
endocrine_patient_data_r5 = [37.1, 36.1, 35.7, 36.7, 39.4]
endocrine_patient_data_r10 = [47.5, 47.6, 47.2, 47.7, 50.1]

# Create the line plot
plt.figure(figsize=(12, 6))

plt.plot(x_labels, upenn_gbm_r5, marker='o', label='UPENN-GBM R@5')
plt.plot(x_labels, upenn_gbm_r10, marker='s', label='UPENN-GBM R@10')
plt.plot(x_labels, endocrine_patient_data_r5, marker='^', label='EndocrinePatientData R@5')
plt.plot(x_labels, endocrine_patient_data_r10, marker='D', label='EndocrinePatientData R@10')

# Customize the chart
plt.title('Impact of the Number of Anchors')
plt.xlabel('K (K\')')
plt.ylabel('Value')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=15)

# Add value labels on each point
for i, (v1, v2, v3, v4) in enumerate(zip(upenn_gbm_r5, upenn_gbm_r10, endocrine_patient_data_r5, endocrine_patient_data_r10)):
    plt.text(i, v1, f'{v1}', ha='left', va='bottom')
    plt.text(i, v2, f'{v2}', ha='right', va='bottom')
    plt.text(i, v3, f'{v3}', ha='left', va='top')
    plt.text(i, v4, f'{v4}', ha='right', va='top')

plt.tight_layout()
plt.show()