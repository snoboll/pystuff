import matplotlib.pyplot as plt

# Data
labels = ["🐨", "🐻", "🧸", "🐻‍❄️"]
values = [10, 15, 14, 100]  # Values for each label; last one is much higher

# Create bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values, color=['blue', 'blue', 'blue', 'red'])  # Make the last bar dramatically different

# Labels and Title
plt.ylabel("Dumheter per tidsenhet")
plt.title("Staple Diagram")
plt.ylim(0, 120)  # Set y limits for better visualization

# Display the plot
plt.tight_layout()
plt.show()
