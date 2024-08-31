
from collections.abc import Mapping

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


models = ['Deep4Net', 'Inception', 'EEGNetv4', 'EEGNetv1', 'Shallow']
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
        # df['best_test_acc'] = df['best_test_acc'].apply(convert_to_numeric)  # Convert 'accuracy' to numeric

        df['best_val_acc'] = df['best_val_acc'].apply(convert_to_numeric)  # Convert 'accuracy' to numeric
        dataframes.append(df)

df_all = pd.concat(dataframes, ignore_index=True)

# Create a new column 'model_subtype' that combines 'model' and 'subtype'
df_all['model_subtype'] = df_all['model'] + "_" + df_all['subtype']

# Create a color palette with a different color for each model
palette_model = dict(zip(df_all['model'].unique(), sns.color_palette('Set2', n_colors=len(df_all['model'].unique()))))

# Map each 'model' to a color
df_all['color'] = df_all['model'].map(palette_model)


# Create a boxplot
box_plot = sns.boxplot(x='model_subtype', y='best_val_acc', data=df_all, hue='model', palette=palette_model)
# box_plot = sns.boxplot(x='model_subtype', y='best_test_acc', data=df_all, hue='model', palette=palette_model)



# Get the medians for each box in the boxplot
medians = df_all.groupby(['model_subtype'])['best_val_acc'].median()
# medians = df_all.groupby(['model_subtype'])['best_test_acc'].median()


# Add model names above the boxes with increased font size
for i, model in enumerate(df_all['model'].unique()):
    # Calculate the midpoint of the three subtypes for each model
    midpoint = i * len(df_all['subtype'].unique()) + len(df_all['subtype'].unique()) / 2 - 0.5
    box_plot.text(x=midpoint, y=df_all['best_val_acc'].max(), s=model, horizontalalignment='center', fontsize=18, verticalalignment='bottom')

# for i, model in enumerate(df_all['model'].unique()):
#     # Calculate the midpoint of the three subtypes for each model
#     midpoint = i * len(df_all['subtype'].unique()) + len(df_all['subtype'].unique()) / 2 - 0.5
#     box_plot.text(x=midpoint, y=df_all['best_test_acc'].max(), s=model, horizontalalignment='center', fontsize=18, verticalalignment='bottom')

plt.title('Box Plot of Best validation Accuracy by Model and Subtype', fontsize=15)
plt.ylabel('Best validation Accuracy', fontsize=16)
plt.legend().remove()
plt.xticks(range(len(df_all['model_subtype'].unique())), df_all['subtype'].unique().tolist() * len(df_all['model'].unique()),fontsize=18)
plt.tight_layout()
plt.show()


# plt.title('Box Plot of Best test Accuracy by Model and Subtype', fontsize=15)
# plt.ylabel('Best test Accuracy', fontsize=16)
# plt.legend().remove()
# plt.xticks(range(len(df_all['model_subtype'].unique())), df_all['subtype'].unique().tolist() * len(df_all['model'].unique()),fontsize=18)
# plt.tight_layout()
# plt.show()