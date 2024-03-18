

# List of models
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to convert accuracy to numeric
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


models = ['deep4net', 'inception', 'eegnetv4', 'eegnetv1', 'shallow']
models1=['deep4.Deep4Net','eeginception_mi.EEGInceptionMI','eegnet.EEGNetv4','eegnet.EEGNetv1','shallow_fbcsp.ShallowFBCSPNet']

# List of subtypes
# subtypes = ['np', 'p', 'pe']
subtypes = ['pe', 'p', 'np']


dataframes = []
for model, model_name in zip(models1, models):
    for subtype in subtypes:
        df = pd.read_excel(f'{subtype}_all_Sub_{model}.xlsx')  # Adjusted file path
        df['model'] = model_name
        df['subtype'] = subtype
        df['best_test_acc'] = df['best_test_acc'].apply(convert_to_numeric)  # Convert 'accuracy' to numeric

        # df['best_val_acc'] = df['best_val_acc'].apply(convert_to_numeric)  # Convert 'accuracy' to numeric
        dataframes.append(df)

df_all = pd.concat(dataframes, ignore_index=True)

# Create a new column 'model_subtype' that combines 'model' and 'subtype'
df_all['model_subtype'] = df_all['model'] + "_" + df_all['subtype']

# Create a color palette with a different color for each model
palette = dict(zip(models, sns.color_palette('Set2', n_colors=len(models))))

# Map each 'model' to a color
df_all['color'] = df_all['model'].map(palette)

# Create a boxplot
# sns.boxplot(x='model_subtype', y='best_val_acc', data=df_all, palette=df_all.set_index('model_subtype')['color'].to_dict())
sns.boxplot(x='model_subtype', y='best_test_acc', data=df_all, palette=df_all.set_index('model_subtype')['color'].to_dict())

plt.title('Box Plot of Best test Accuracy by Model and Subtype', fontsize=15)
plt.xlabel('Model_Subtype', fontsize=12)
plt.ylabel('Best test Accuracy', fontsize=12)
# plt.title('Box Plot of Best validation Accuracy by Model and Subtype', fontsize=15)
# plt.xlabel('Model_Subtype', fontsize=12)
# plt.ylabel('Best validation Accuracy', fontsize=12)

plt.xticks(rotation=360)  # Rotate x-axis labels for better visibility

plt.tight_layout()
plt.show()