


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def convert_to_numeric(val):
    try:
        return float(val)
    except ValueError:
        parts = val.split(" ")
        if len(parts) > 5:
            try:
                return float(parts[5].replace(',', ''))  # Remove commas before converting to float
            except ValueError:
                return None  # or some other value indicating an error
        else:
            return None  # or some other value indicating an error

# List of subjects
subjects = range(1, 10)

# List of models
models = ['Within']

# List of types
# types = ['np', 'p', 'pe']
types = ['pe', 'p', 'np']

dataframes = []
for subject in subjects:
    for data_type in types:
        for model in models:
            df = pd.read_excel(f'{data_type}_{model}_Sub_{subject}_deep4.Deep4Net.xlsx')
            df['type'] = data_type
            df['subject'] = subject
            df['model'] = model
            df['best_val_acc'] = df['best_val_acc'].apply(convert_to_numeric)  # Convert 'best_val_acc' to numeric

            # df['best_test_acc'] = df['best_test_acc'].apply(convert_to_numeric)  # Convert 'best_val_acc' to numeric
            dataframes.append(df)

df_all = pd.concat(dataframes, ignore_index=True)

# Create a new column 'subject_type' that combines 'subject' and 'type'
df_all['subject_type'] = df_all['subject'].astype(str) + "_" + df_all['type']

# Order the 'subject_type' column by 'subject' and 'type'
df_all['subject_type'] = pd.Categorical(df_all['subject_type'], categories=[f"{subject}_{type}" for subject in subjects for type in types], ordered=True)

# Sort the dataframe by 'subject_type'
df_all = df_all.sort_values('subject_type')

# Create a color palette with a different color for each subject
palette = dict(zip(df_all['subject'].unique(), sns.color_palette('Set2', n_colors=len(df_all['subject'].unique()))))

# Map each 'subject' to a color
df_all['color'] = df_all['subject'].map(palette)

# Create a boxplot
# sns.boxplot(x='subject_type', y='best_test_acc', data=df_all, palette=df_all.set_index('subject_type')['color'].to_dict())
sns.boxplot(x='subject_type', y='best_val_acc', data=df_all, palette=df_all.set_index('subject_type')['color'].to_dict())

plt.title('Box Plot of Best Validation Accuracy by Subject and Type', fontsize=15)
plt.xlabel('Subject_Type', fontsize=12)
plt.ylabel('Best validation Accuracy', fontsize=12)
# plt.title('Box Plot of Best test Accuracy by Subject and Type', fontsize=15)
# plt.xlabel('Subject_Type', fontsize=12)
# plt.ylabel('Best test Accuracy', fontsize=12)


plt.tight_layout()
plt.xticks(rotation=360)  # Rotate x-axis labels for better visibility
plt.show()