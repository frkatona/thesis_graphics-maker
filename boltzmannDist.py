import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

# Constants
k = 1.38e-23  # Boltzmann's constant, J/K

def maxwell_boltzmann(E, T):
    """Calculate the Maxwell-Boltzmann distribution."""
    return np.sqrt(2/np.pi) * (E**0.5) * np.exp(-E/(k*T)) / (k*T)**1.5

# Energy range for plotting
E_scaled = np.linspace(0, 20 * 0.75e-20, 1000)

# Temperatures to consider
temperatures = [200, 273, 500, 1000, 2000]

# Calculate the Maxwell-Boltzmann distributions for the temperatures
functions = [maxwell_boltzmann(E_scaled, T) for T in temperatures]

# Sort by temperature for consistent color mapping
sorted_indices = np.argsort(temperatures)
temperatures_sorted = np.array(temperatures)[sorted_indices]
functions_sorted = np.array(functions)[sorted_indices]

# Color map for plotting
colors = plt.cm.jet(np.linspace(0, 1, len(temperatures_sorted)))

# Plotting
plt.figure(figsize=(10, 6))
for i, T in enumerate(temperatures_sorted):
    plt.plot(E_scaled, functions_sorted[i], color=colors[i])
    # Annotate the temperature near the peak of each curve
    annotation_x = E_scaled[np.argmax(functions_sorted[i])]
    annotation_y = max(functions_sorted[i])
    plt.annotate(f'{T} K', (annotation_x, annotation_y), textcoords="offset points", xytext=(10,10), ha='center',
                 fontsize=2*plt.rcParams['font.size'], color=colors[i],
                 path_effects=[pe.withStroke(linewidth=3, foreground='black')])

plt.xlabel('Kinetic Energy')
plt.ylabel('Fraction of Molecules')
plt.xticks([])  # Remove x-axis numbers
plt.yticks([])  # Remove y-axis numbers
plt.tight_layout()
plt.show()
