import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:/WorldCupMatches.csv')

# Print the shape of the DataFrame
rows, columns = df.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")

# Print each column name
print("Column names:")
for col in df.columns:
    print(col)

# Print specific range using slicing (e.g., rows 10 to 20)
print("Slicing rows from index 10 to 20:")
print(df.iloc[10:21])

# Summarization statistics
print("Summarization statistics:")
print(df.describe())

# Check for missing values
print("Checking for missing values:")
print(df.isnull().sum())

# Replace missing numerical values with mean
for col in df.columns:
    if df[col].isnull().sum() > 0:
        if df[col].dtype in ['int64', 'float64']:
            df[col].fillna(df[col].mean(), inplace=True)

# Pairplot
sns.pairplot(df.select_dtypes(include=['float64', 'int64']))
plt.show()

# Heatmap
numerical_df = df.select_dtypes(include=['float64', 'int64'])
corr = numerical_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

# Barplot
plt.figure(figsize=(9, 5))
sns.barplot(x='Home Team Name', y='Home Team Goals', data=df.head(10))
plt.xticks(rotation=45)
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Home Team Goals'], bins=30, kde=True)
plt.show()

# Distribution Plot
plt.figure(figsize=(10, 6))
sns.histplot(df['Home Team Goals'], bins=30, kde=True)
plt.show()

# Scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Home Team Goals', y='Away Team Goals', data=df)
plt.show()

# Check for missing values again
print(df.isnull().sum())

# Print the shape of the DataFrame again
print(df.shape)

# Summarization statistics again
print(df.describe())

# Print a specific column
print(df['Home Team Name'])

# Max and min values
max_value = df['Home Team Goals'].max()
min_value = df['Home Team Goals'].min()
print(f"Max value in Home Team Goals: {max_value}")
print(f"Min value in Home Team Goals: {min_value}")
