import matplotlib
matplotlib.use('TkAgg')  # Use an interactive backend, if available

import numpy as np
import matplotlib.pyplot as plt

# Define the parametric equations for the surface (e.g., a torus)
def parametric_torus(R, r, u, v):
    x = (R + r * np.cos(v)) * np.cos(u)
    y = (R + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v)
    return x, y, z

# Parameters
R, r = 3, 1
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, 2 * np.pi, 50)
u, v = np.meshgrid(u, v)
x, y, z = parametric_torus(R, r, u, v)

# Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='k')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("Parametric Surface: Torus")

# Save the plot or display it
try:
    plt.show()  # Try displaying the plot
except:
    plt.savefig("parametric_surface.png")  # Save as an image if display fails
    print("Interactive display not available. Plot saved as parametric_surface.png")
