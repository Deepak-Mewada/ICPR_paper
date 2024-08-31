import numpy as np

# Example data: multiple accuracy measurements for "EEGNet v4"
accuracies = [74.56, 75.12, 73.98, 74.85, 74.20]  # Replace with actual data if available

# Calculate the mean accuracy
mean_accuracy = np.mean(accuracies)

# Calculate the standard deviation
std_dev_accuracy = np.std(accuracies)

print(f"Mean Accuracy: {mean_accuracy:.2f}%")
print(f"Standard Deviation: {std_dev_accuracy:.2f}%")