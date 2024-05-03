import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
import matplotlib as mpl # type: ignore

# Setting formatting parameters for matplotlib
mpl.rcParams['lines.linewidth'] = 1  # Setting line width
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 6  # Setting figure size for x-axis
fig_size[1] = fig_size[0] / 1.3  # Setting figure size for y-axis
plt.rcParams["figure.figsize"] = fig_size

# Setting text rendering to LaTeX
plt.rcParams.update({
    "text.usetex": 1,
    "font.family": "serif",
    "font.sans-serif": ["Helvetica"]
})

# Setting parameters for legend and markers
plt.rcParams['legend.frameon'] = False
plt.rcParams['legend.handlelength'] = 2.0
plt.rcParams['lines.markersize'] = 5

# Setting font parameters
plt.rc('font', size=12)          # controls default text sizes
plt.rc('axes', titlesize=18)    # fontsize of the axes title
plt.rc('axes', labelsize=14)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels
plt.rc('legend', fontsize=0)       # legend fontsize
plt.rc('figure', titlesize=0)  # fontsize of the figure title

# Value dump (rounded to 3 significant figures)
pva_ca = (61.5, 61.9, 64.2, 37.3)
pva_ca_bcd_4_1 = (70.8, 66.3, 68.1, 70.8)
pva_ca_bcd_2_1 = (86.6, 80.2, 81.3, 88.5)
pva_bcd_4_1 = (69.5, 75.6, 74.4, 72.2)

# Calculate medians for each dataset
medians = [np.median(pva_ca), np.median(pva_ca_bcd_4_1), np.median(pva_ca_bcd_2_1), np.median(pva_bcd_4_1)]

# Combine all data points into a single array
all_data = np.concatenate([pva_ca, pva_ca_bcd_4_1, pva_ca_bcd_2_1, pva_bcd_4_1])

# Initialize labels for the plot
labels = ['PVA + CA'] * len(pva_ca) + [r"{4:1 PVA-}$\beta${CD + CA}"] * len(pva_ca_bcd_4_1) + [r"{2:1 PVA-}$\beta${CD + CA}"] * len(pva_ca_bcd_2_1) + [r"{4:1 PVA-}$\beta${CD}"] * len(pva_bcd_4_1)

# Create the plot
plt.figure(figsize=(10, 6))  # Adjust figure size for slides/paper/poster
sns.stripplot(x=labels, y=all_data, jitter=True, alpha=0.5, marker='o', color='blue')  # Create categorical scatter plot
plt.title(r'Swelling of PVA Hydrogels')
plt.ylabel(r'Swelling Capacity (\% weight)')

# Plot median lines for each dataset
for i, median in enumerate(medians):
    plt.plot([i - 0.2, i + 0.2], [median, median], color='blue',)

plt.savefig("swellingAnalysis.svg", format="svg")

