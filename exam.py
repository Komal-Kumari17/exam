# Importing required libraries for this project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data preprocessing
df = pd.read_csv("exams (1).csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print("First five rows are :")
print(df.head())
print("Last five rows are : ")
print(df.tail())
print(df.info())


# Replace spaces in the column names with underscore
df.columns = [c.replace(" ","_") for c in df.columns]
print("Updated Columns:\n")
print(df.columns)


# Checking missing values
check = pd.isnull(df).sum()
print("Checking whether any null value in dataset or not.")
print(check)


# Identifying outliers range
a = np.percentile(df["writing_score"],25)
b = np.percentile(df["writing_score"],75)
iqr = b - a
lower = a -(1.5*iqr)
upper = b +(1.5*iqr)
print(" Interquartile Range is: ",lower,",",upper)
# We can see in range that there are almost no outliers because each value is in range.
# df.boxplot("writing_score")
# plt.show()


# Checking data points
# print(df["writing_score"])


# Exploratory data analysis
print("Shape of the dataset:\n",df.shape)
print("Size of the dataset:\n",df.size)
print("Dimension of the dataset:\n",df.ndim)
print("Maximum 5 marks in Math:\n",df.nlargest(5,"math_score"))
print("Maximum 5 marks in Reading:\n",df.nlargest(5,"reading_score"))
print("Maximum 5 marks in Writing:\n",df.nlargest(5,"writing_score"))
print("\n")

# Grouping by gender to check gender base performance
gender_comparison = df.groupby("gender")[["math_score","reading_score","writing_score"]].mean()
print(gender_comparison)
# Visualizing the comparisons
gender_comparison.plot(kind='bar', figsize=(8,5))
plt.title("Average Scores by Gender")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.legend(title="Subjects")
plt.grid(axis='y')
plt.show()
print("The averages show male candidates have high performance in math score as comparison to female candidates and female candidates have higher performance in reading and writing subject.\n")


# Grouping by test preparation course completion to check whether test preparation help in performance
prep_comparison = df.groupby("test_preparation_course")[["math_score", "reading_score", "writing_score"]].mean()
print(prep_comparison)
# Visualizing the comparisons
prep_comparison.plot(kind = 'bar',figsize =(8,5))
plt.title("Average Scores by Test Preparation")
plt.ylabel("Average score")
plt.xticks(rotation = 0)
plt.legend(title = "Subjects")
plt.grid(axis ='y')
plt.show()
print("The averages are consistently higher for students who completed the test preparation course, so we can conclude that test preparation has positive effect on student's performance.\n")


# Identify most struggled subject using average
subject_averages = df[["math_score", "reading_score", "writing_score"]].mean()
print(subject_averages)
# Identify the subject with the lowest average score
struggled_subject = subject_averages.idxmin()
lowest_score = subject_averages.min()
# Visualilzing the comparisons
subject_averages.plot(kind='bar', color='salmon')
plt.title("Average Scores by Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()
print(f"\nStudents struggle the most in: {struggled_subject} (average score: {lowest_score:.2f})\n")


# Calculating correlation between subjects
correlation = df[["math_score", "reading_score", "writing_score"]].corr()
print(correlation)
# Visualization(Heatmap) of correlations
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Between Subjects")
plt.show()

# sns.boxplot(data=df, x='test_preparation_course', y='math_score') 
# plt.title("Math Score vs Test Preparation") 
# plt.show()
