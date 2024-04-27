import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np

# Assuming you have your data in 2D arrays: accuracies, standard_deviations
models = ['Shallow FBCSP', 'CTCNN', 'EEGNet v4', 'Inception MI', 'Deep4Net']
subjects = ['Subject1', 'Subject2', 'Subject3', 'Subject4', 'Subject5', 'Subject6', 'Subject7', 'Subject8', 'Subject9']

#cross
accuracies = np.array([[61.30, 62.291, 67.62,51.11 , 56.64], [46.97,51.336,54.04,40.67,46.441],[73.4722,71.14,71.57,60.034,73.4201],[51.19,50.85,53.81,42.70,50.72],[55.468,56.163,60.71,41.73,57.5],[54.28,58.055,57.482,42.91,53.50],[69.04,66.89,68.64,57.361,65.83],[70.41,69.40,69.94,59.79,63.78],[62.06,59.93,63.75,51.78,59.21] ]) # replace with your actual 2D array
standard_deviations = np.array([[1.48,4.96,1.10,1.91,2.11],[1.31,2.69,1.63,2.05,2.22],[1.19,2.14,2.07,3.51,1.79],[1.88,2.02,2.08,1.79,0.94],[3.23,1.85,1.941,3.79,1.83],[1.86,3.25,3.20,1.75,1.32],[1.41,1.96,2.81,2.44,1.49],[1.20,2.89,2.03,1.930,2.30],[1.37,1.44,1.06,3.20,1.55]]) # replace with your actual 2D array

#within
# accuracies = np.array([[56.72,54.13,61.89,47.49,51.98], [27.41,36.03,37.5,24.48,27.84],[55.77,61.29,70.94,53.62,47.84],[43.53,44.74,49.82,33.70,39.39],[31.89,36.55,35.68,30.68,29.05],[36.46,33.18,40.00,28.70,27.67],[46.72,40.25,43.18,36.81,26.20 ],[47.93,58.62,61.63,52.58,41.03],[55.68,63.44,68.27,53.27,60.94]]) # replace with your actual 2D array
# standard_deviations = np.array([[2.75,4.19,3.63,7.90,5.74],[2.95,2.53,3.75,1.58,2.87],[4.22,8.89,3.44,4.77,2.76],[1.96,2.00,4.92,2.99,4.12],[3.70,5.47,3.35,5.25,2.22],[3.66,5.77,3.9,5.28,2.09],[4.41,4.47,6.36,4.91,3.52],[3.33,3.49,2.48,5.66,8.83],[3.15,4.93,3.56,6.49,3.94]]) # replace with your actual 2D array

# Create lists for Model, Subject, Accuracy and Standard Deviation
model_list = []

subject_list = []
accuracy_list = []
std_dev_list = []

for i, subject in enumerate(subjects):
    for j, model in enumerate(models):
        model_list.append(model)
        subject_list.append(subject)
        accuracy_list.append(accuracies[i][j])
        std_dev_list.append(standard_deviations[i][j])


df = pd.DataFrame({
    'Model': model_list,
    'Subject': subject_list,
    'Accuracy': accuracy_list,
    'Std Dev': std_dev_list
})

# Define a color palette
palette = sns.color_palette('Set2', len(df['Model']))

# # Create a box plot without outliers
# plt.figure(figsize=(10, 6))
# sns.boxplot(x='Model', y='Accuracy', data=df, showfliers=False,palette=palette)
# sns.swarmplot(x='Model', y='Std Dev', data=df, color=".25")
# plt.title('Within subject accuracy on BCI-IV 2a data set')
# plt.ylim(20,80)  # Set the limits of the y-axis
# plt.show()

# Create a box plot without outliers
plt.figure(figsize=(10, 6))
box_plot = sns.boxplot(x='Model', y='Accuracy', data=df, showfliers=False, palette=palette)
sns.swarmplot(x='Model', y='Std Dev', data=df, color=".25")

# Add names above the boxes with increased font size
for i in range(len(df['Model'].unique())):
    plt.text(x=i, y=df['Accuracy'].max() + 1, s=df['Model'].unique()[i], horizontalalignment='center', fontsize=16)

# Remove x-axis label and ticks
plt.xlabel('')
plt.xticks([])

# Increase the font size of the title and the y-axis label
plt.title('Cross subject accuracy on BCI-IV 2a dataset', fontsize=16)
plt.ylabel('Accuracy Percentage', fontsize=14)

plt.ylim(40,80)  # Set the limits of the y-axis
plt.show()