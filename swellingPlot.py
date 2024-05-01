import matplotlib.pyplot as plt  # type: ignore
import numpy as np # type: ignore

# value dump (3 sig figs)
pva_ca = np.random.normal(61.5, 61.9, 100)
test2_scores = np.random.normal(75, 8, 100)
test3_scores = np.random.normal(80, 12, 100)
test4_scores = np.random.normal(85, 9, 100)

#initialize graph
all_scores = [pva_ca, test2_scores, test3_scores, test4_scores]
plt.boxplot(all_scores)

# title/labels
plt.title('PVA Gel Swelling %')
plt.ylabel('Swelling Capacity (%wt)')
plt.xticks([1, 2, 3, 4], ['PVA-CA', '4:1 PVA-CA-BCD', '2:1 PVA-CA-BCD', '4:1 PVA-BCD'])

# show
plt.show()
