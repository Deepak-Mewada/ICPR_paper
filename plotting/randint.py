# import matplotlib.pyplot as plt

# # Data for x and y axes based on the description
# x = [100, 150, 200, 250,252.5,300, 350, 400, 450, 500]
# y = [80, 78, 73, 74, 50,50,50, 50, 50, 50]

# # Create a plot
# plt.figure(figsize=(12, 6))  # Set the figure size if needed

# # Plot the data
# plt.plot(x, y, 'b-', marker='o')  # 'b-' means a blue line, and marker='o' adds circle markers

# # Set x and y axis labels
# plt.xlabel('Sampling Rate')
# plt.ylabel('Accuracy')

# # Set axis limits to start x-axis from 0
# plt.xlim(0, max(x))
# plt.ylim(45, 85)

# # Display the plot
# plt.show()

# import matplotlib.pyplot as plt

# # Data for x and y axes based on the description
# x = [100, 150, 200, 250, 252.5, 300, 350, 400, 450, 500]
# y = [80, 78, 73, 74, 50, 50, 50, 50, 50, 50]

# # Create a plot
# plt.figure(figsize=(12, 6))  # Set the figure size

# # Plot the data
# plt.plot(x, y, 'b-', marker='o')  # 'b-' means a blue line, and marker='o' adds circle markers

# # Set x and y axis labels
# plt.xlabel('Sampling Rate')
# plt.ylabel('Accuracy')

# # Set specific ticks for x and y axes
# plt.xticks([100, 150, 200, 250, 300, 350, 400, 450, 500])
# plt.yticks([50, 60, 70, 80, 90, 100])

# # Set axis limits to make sure the ticks are displayed properly
# plt.xlim(90, 510)
# plt.ylim(45, 105)

# # Display the plot
# plt.show()

import matplotlib.pyplot as plt

# Data for x and y axes based on the description
x = [100, 150, 200, 250, 252.5, 300, 350, 400, 450, 500]
y = [80, 78, 73, 74, 50, 50, 50, 50, 50, 50]

# Create a plot
plt.figure(figsize=(12, 6))  # Set the figure size

# Plot the data
plt.plot(x, y, 'b-', marker='o')  # 'b-' means a blue line, and marker='o' adds circle markers

# Set x and y axis labels with increased font size
plt.xlabel('Sampling Rate', fontsize=14)
plt.ylabel('Accuracy(%)', fontsize=14)

# Set specific ticks for x and y axes with increased font size for ticks
plt.xticks([100, 150, 200, 250, 300, 350, 400, 450, 500], fontsize=12)
plt.yticks([50,55, 60,65, 70,75, 80], fontsize=15)

# Set axis limits to make sure the ticks are displayed properly
plt.xlim(90, 510)
plt.ylim(45, 85)

# Display the plot
plt.show()