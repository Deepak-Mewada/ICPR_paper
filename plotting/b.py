# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Define your data
data = {
    'model': ['Shallow FBCSP', 'EEGNet v1', 'EEGNet v4', 'Inception MI', 'Deep4Net'],
    'accuracy': [62.31,67.52,74.56,55.46,63.21]
}

df = pd.DataFrame(data)

# Define a color palette
palette = sns.color_palette('Set2', len(data['model']))

# Create a bar plot
sns.barplot(x='model', y='accuracy', data=df, palette=palette)

# Add model names above the bars with increased font size
for i in range(len(df['model'])):
    plt.text(x=i, y=df['accuracy'][i] + 1, s=df['model'][i], horizontalalignment='center', fontsize=12)

# Remove x-axis label and ticks
plt.xlabel('')
plt.xticks([])

plt.ylabel('Accuracy Percentage', fontsize=14)
plt.title('Cross subject accuracy on Cho-2017 dataset', fontsize=16)
plt.ylim(20,90)
plt.show()