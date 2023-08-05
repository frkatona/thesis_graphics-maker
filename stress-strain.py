import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from matplotlib.animation import FuncAnimation

# Define strain values
strain = np.linspace(0, 1, 500)

# Define initial stress values
stress = np.piecewise(strain, 
                      [strain <= 0.1, (strain > 0.1) & (strain <= 0.3), strain > 0.3],
                      [lambda x: 10*x, 
                       lambda x: 1 + 15*(x-0.1), 
                       lambda x: 4 + 0.5*(x-0.3)])

# Create more points for a smoother curve
xnew = np.linspace(strain.min(), strain.max(), 500) 

# Apply initial B-spline interpolation
spl = make_interp_spline(strain, stress, k=3)
power_smooth = spl(xnew)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
line, = ax.plot(xnew, power_smooth)
ax.set_xlabel(r'$\epsilon$ (Strain)', fontsize=14)
ax.set_ylabel(r'$\sigma$ (Stress)', fontsize=14)
ax.grid(True)

def update(num):
    # Update stress values with increasing slope in the linear region
    stress = np.piecewise(strain, 
                          [strain <= 0.1, (strain > 0.1) & (strain <= 0.3), strain > 0.3],
                          [lambda x: 10*x, 
                           lambda x: 1 + (15 + num)*(x-0.1), 
                           lambda x: 4 + 0.5*(x-0.3)])

    # Apply updated B-spline interpolation
    spl = make_interp_spline(strain, stress, k=3)
    power_smooth = spl(xnew)

    # Update plot
    line.set_ydata(power_smooth)
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), blit=True)

# Save the animation as an mp4 file
ani.save('stress_strain_animation.mp4', writer='ffmpeg')

plt.show()
