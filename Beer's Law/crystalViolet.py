import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from scipy.stats import linregress # type: ignore

# Data points
x = np.array([4, 8, 13, 18])
y = np.array([0.360, 0.738, 1.099, 1.367])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Define the regression line
x_fit = np.linspace(0, 20, 100)  # Extend the range to cover the full x-axis
regression_line = slope * x_fit + intercept

# Set up LaTeX rendering
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Font Settings
plt.rc('font', size=12)          # controls default text sizes
plt.rc('axes', titlesize=18)    # fontsize of the axes title

# Plot the data points and regression line
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='black', s=8, label='Spectrophotometer Readings')  # Adjust the 's' parameter to make dots smaller
plt.plot(x_fit, regression_line, linewidth = 1.2, color='#7F00FF', label=rf'Fit: $y = {slope:.2f}x + {intercept:.4f}$' '\n' rf'$R^2 = {r_value**2:.4f}$')

# Darken the axes at x=0 and y=0
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Add titles and labels
plt.title(r'Crystal Violet Standard Curve')
plt.xlabel(r'Molarity ($ \mu M$)')
plt.ylabel(r'Absorbance (590.4 nm)')
plt.legend()

# Save plot
plt.grid(True)
plt.savefig("crystalViolet.svg", format="svg")
