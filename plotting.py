import matplotlib.pyplot as plt
import numpy as np

x_points = [0]
y_points = [0]
prev_distance = 0

with open("coverage_log.txt", "r") as file:
    for line in file:
        if not line.strip():
            continue
        distance, angle = map(float, line.strip().split(','))
        
        delta_d = distance - prev_distance
        
        rad = np.radians(angle)
        new_x = x_points[-1] + delta_d * np.sin(rad)
        new_y = y_points[-1] + delta_d * np.cos(rad)
        
        x_points.append(new_x)
        y_points.append(new_y)
        prev_distance = distance

plt.figure(figsize=(10, 8))
plt.plot(x_points, y_points, label="Robot Coverage Path", color="blue", linewidth=2)
plt.scatter(x_points[0], y_points[0], color="green", marker="o", s=120, zorder=5, label="Start Position (Corner)")
plt.scatter(x_points[-1], y_points[-1], color="red", marker="x", s=120, zorder=5, label="End Position")

plt.title("Robot Area Coverage Blueprint (High Resolution)")
plt.xlabel("X Position (mm)")
plt.ylabel("Y Position (mm)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.axis("equal")

plt.savefig("robot_coverage_map.png", dpi=300, bbox_inches="tight")

plt.show()
