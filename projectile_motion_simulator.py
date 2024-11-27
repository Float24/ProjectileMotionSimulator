import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def simulate():
    try:
        # Retrieve inputs
        velocity = float(velocity_entry.get())
        angle_deg = float(angle_entry.get())
        height = float(height_entry.get())
        
        angle_rad = np.radians(angle_deg)
        g = 9.8

        # Horizontal and vertical velocity components
        vX = velocity * np.cos(angle_rad)
        vY = velocity * np.sin(angle_rad)

        # Time of flight, max height, and range
        time_of_flight = (vY + np.sqrt(vY**2 + 2 * g * height)) / g
        max_height = height + (vY**2) / (2 * g)
        range_ = vX * time_of_flight

        # Display results
        time_of_flight_label.config(text=f"Time of Flight: {time_of_flight:.2f} s")
        max_height_label.config(text=f"Max Height: {max_height:.2f} m")
        range_label.config(text=f"Range: {range_:.2f} m")

        # Plot the trajectory
        plot_trajectory(vX, vY, g, height, time_of_flight)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values.")

def plot_trajectory(vX, vY, g, height, time_of_flight):
    t = np.linspace(0, time_of_flight, num=500)
    x = vX * t
    y = height + vY * t - 0.5 * g * t**2

    # Clear previous plots
    ax.clear()
    ax.plot(x, y, label="Trajectory")
    ax.set_title("Projectile Motion Trajectory")
    ax.set_xlabel("Horizontal Distance (m)")
    ax.set_ylabel("Vertical Height (m)")
    ax.legend()
    ax.grid()
    canvas.draw()

def reset():
    velocity_entry.delete(0, tk.END)
    angle_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    time_of_flight_label.config(text="Time of Flight: ")
    max_height_label.config(text="Max Height: ")
    range_label.config(text="Range: ")
    ax.clear()
    ax.set_title("Projectile Motion Trajectory")
    ax.set_xlabel("Horizontal Distance (m)")
    ax.set_ylabel("Vertical Height (m)")
    canvas.draw()

# Create the main window
root = tk.Tk()
root.title("Projectile Motion Simulator")

# Input fields
tk.Label(root, text="Initial Velocity (m/s):").grid(row=0, column=0, padx=10, pady=5)
velocity_entry = tk.Entry(root)
velocity_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Angle (degrees):").grid(row=1, column=0, padx=10, pady=5)
angle_entry = tk.Entry(root)
angle_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Initial Height (m):").grid(row=2, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1, padx=10, pady=5)

# Buttons
simulate_button = tk.Button(root, text="Simulate", command=simulate)
simulate_button.grid(row=3, column=0, padx=10, pady=10)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(row=3, column=1, padx=10, pady=10)

# Output labels
time_of_flight_label = tk.Label(root, text="Time of Flight: ")
time_of_flight_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

max_height_label = tk.Label(root, text="Max Height: ")
max_height_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

range_label = tk.Label(root, text="Range: ")
range_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Matplotlib figure
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_title("Projectile Motion Trajectory")
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Height (m)")
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=2, rowspan=7, padx=10, pady=5)

# Run the application
root.mainloop()
