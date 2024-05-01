import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns # type: ignore
import numpy as np # type: ignore

# value dump (3 sig figs)
pva_ca = (61.5, 61.9, 64.2)
pva_ca_bcd_4_1 = (70.8, 66.3, 68.1, 70.8)
pva_ca_bcd_2_1 = (86.6, 80.2, 81.3, 88.5)
pva_bcd_4_1 = (85.9, 100.0)

# Calculate medians
medians = [np.median(pva_ca), np.median(pva_ca_bcd_4_1), np.median(pva_ca_bcd_2_1), np.median(pva_bcd_4_1)]

# Combine data
all_data = np.concatenate([pva_ca, pva_ca_bcd_4_1, pva_ca_bcd_2_1, pva_bcd_4_1])

# initialization
labels = ['PVA-CA'] * len(pva_ca) + ['4:1 PVA-CA-BCD'] * len(pva_ca_bcd_4_1) + ['2:1 PVA-CA-BCD'] * len(pva_ca_bcd_2_1) + ['4:1 PVA-BCD'] * len(pva_bcd_4_1)
plt.figure(figsize=(10, 6))  # Adjust figure size for slides/paper/poster
sns.stripplot(x=labels, y=all_data, jitter=True, alpha=0.5, marker='o')  #categorical scatter plot
plt.title('PVA Gel Swelling %')
plt.ylabel('Swelling Capacity (%wt)')
plt.xlabel('Tests')

# median lines
for i, median in enumerate(medians):
    plt.plot([i - 0.2, i + 0.2], [median, median], color='black', lw=1)

plt.show()
