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
values = [40.84, 40.19, 40.18, 40.40, 40.20]
errors = [0.094, 0.043, 0.20, 0.07, 0.20]

# Set up LaTeX rendering
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Create the plot
fig, ax = plt.subplots()

# Plot with error bars
ax.errorbar(categories, values, yerr=errors, fmt='o', ecolor='r', capsize=5, linestyle='None', marker='s', mfc='blue', mec='blue')

# Labels and title in LaTeX
ax.set_ylabel(r'\textbf{Pb}$^{2+}$ \textbf{in 10mL aliquots (mg)}', fontsize=14)
ax.set_title(r'\textbf{Pb}$^{2+}$ \textbf{Removal Viability}', fontsize=16)


# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# Display grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to make room for the rotated x-axis labels
plt.tight_layout()

# Show the plot
plt.show()
