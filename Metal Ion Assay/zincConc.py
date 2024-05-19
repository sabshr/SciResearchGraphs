import matplotlib.pyplot as plt
import numpy as np

# Data from the table
categories = [
    'Control (no gel)', 
    'PVA + CA', 
    'PVA/B-CD', 
    'PVA/B-CD(4:1) + CA', 
    'PVA/B-CD(2:1) + CA'
]
values = [4.18, 4.05, 3.99, 4.12, 4.179]
errors = [0.09, 0.03, 0.11, 0.06, 0.004]

# Set up LaTeX rendering
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Create the plot
fig, ax = plt.subplots()

# Plot with error bars
ax.errorbar(categories, values, yerr=errors, fmt='o', ecolor='r', capsize=5, linestyle='None', marker='s', mfc='blue', mec='blue')
# Labels and title in LaTeX
ax.set_ylabel(r'\textbf{Zn}$^{2+}$ \textbf{in 10mL aliquots (mg)}', fontsize=14)
ax.set_title(r'\textbf{Zn}$^{2+}$ \textbf{Removal Viability}', fontsize=16)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# Display grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to make room for the rotated x-axis labels
plt.tight_layout()

# Save plot
plt.savefig("zincConc.svg", format="svg")
