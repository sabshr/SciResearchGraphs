import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from scipy.stats import linregress # type: ignore

# Data points
x = np.array([0.034, 0.067, 0.101, 0.134])
y = np.array([0.320, 0.627, 0.902, 1.145])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Define the regression line
x_fit = np.linspace(-0, 0.138, 10)  # Extend the range to cover the full x-axis
regression_line = slope * x_fit + intercept

# Set up LaTeX rendering
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Plot the data points and regression line
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='black', s=10, label='Data points')  # Adjust the 's' parameter to make dots smaller
plt.plot(x_fit, regression_line, linewidth = 0.8, color='#DC143C', label=rf'Fit: $y = {slope:.2f}x + {intercept:.4f}$' '\n' rf'$R^2 = {r_value**2:.4f}$')

# Darken the axes at x=0 and y=0
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Add titles and labels
plt.title(r'Congo Red Standard Curve')
plt.xlabel(r'Molarity ($ \mu M$)')
plt.ylabel(r'Absorbance (498.8 nm)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
