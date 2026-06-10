import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Student Mental Health Analysis During Online Learning.csv")

# Remove 'Other' gender (only 1 record)
df = df[df['Gender'] != 'Other']

# Dataset overview
print("Columns:")
print(df.columns.tolist())

print("\nGender Count:")
print(df['Gender'].value_counts())

print("\nEducation Level Count:")
print(df['Education Level'].value_counts())

# Create Anxiety Score
df['Anxiety Score'] = df['Anxious Before Exams'].map({
    'No': 0,
    'Yes': 1
})

# Grouped data

screen_gender = df.groupby(
    ['Education Level', 'Gender']
)['Screen Time (hrs/day)'].mean().unstack()

sleep_gender = df.groupby(
    ['Education Level', 'Gender']
)['Sleep Duration (hrs)'].mean().unstack()

anxiety_gender = df.groupby(
    ['Education Level', 'Gender']
)['Anxiety Score'].mean().unstack()

activity_gender = df.groupby(
    ['Education Level', 'Gender']
)['Physical Activity (hrs/week)'].mean().unstack()

# Dashboard (2 x 2)

fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# Screen Time
screen_gender.plot(
    kind='bar',
    ax=axes[0, 0]
)
axes[0, 0].set_title('Average Screen Time')
axes[0, 0].set_xlabel('Education Level')
axes[0, 0].set_ylabel('Hours per Day')
axes[0, 0].tick_params(axis='x', rotation=45)

# Sleep Duration
sleep_gender.plot(
    kind='bar',
    ax=axes[0, 1]
)
axes[0, 1].set_title('Average Sleep Duration')
axes[0, 1].set_xlabel('Education Level')
axes[0, 1].set_ylabel('Hours')
axes[0, 1].tick_params(axis='x', rotation=45)

# Exam Anxiety
anxiety_gender.plot(
    kind='bar',
    ax=axes[1, 0]
)
axes[1, 0].set_title('Average Exam Anxiety')
axes[1, 0].set_xlabel('Education Level')
axes[1, 0].set_ylabel('Anxiety Score')
axes[1, 0].tick_params(axis='x', rotation=45)

# Physical Activity
activity_gender.plot(
    kind='bar',
    ax=axes[1, 1]
)
axes[1, 1].set_title('Average Physical Activity')
axes[1, 1].set_xlabel('Education Level')
axes[1, 1].set_ylabel('Hours per Week')
axes[1, 1].tick_params(axis='x', rotation=45)

# Main title
fig.suptitle(
    'Student Mental Health Analysis During Online Learning',
    fontsize=16,
    fontweight='bold'
)

plt.tight_layout()

# Save for LinkedIn / Portfolio
plt.show()




df['Education Level'].value_counts().plot(
    kind='bar',
    figsize=(10,5)
)

plt.title('Student Distribution by Education Level')
plt.show()