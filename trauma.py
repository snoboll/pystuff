import matplotlib.pyplot as plt
import numpy as np

# Create a figure and an axis
fig, ax = plt.subplots()

# Define time intervals
x1 = np.linspace(0, 7, 100)
x2 = np.linspace(7, 15, 100)
x3 = np.linspace(15, 30, 100)

# Define corresponding scores for the intervals
y1 = np.full_like(x1, 100)  # Constant score of +100 for <7 mins
y2 = np.linspace(99, 0, 100)  # Linear decrease from 99 to 0 for 7-15 mins
y3 = np.linspace(-1, -200, 100)  # Linear decrease from -1 to -200 for 15-30 mins

# Plot for each interval
ax.plot(x1, y1, label='0-7 mins (+100 points)')
ax.plot(x2, y2, label='7-15 mins (99 to 0 points)')
ax.plot(x3, y3, label='15-30 mins (-1 to -200 points)')

# Set labels and title
ax.set_xlabel('Time (minutes)')
ax.set_ylabel('Score')
ax.set_title('Score vs Time')

# Display the legend
ax.legend()

# Show the plot
plt.show()
