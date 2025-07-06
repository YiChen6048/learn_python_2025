# Middle Level Student Scores Analysis
# Skills practiced: Control Structures, Function Definition, DataFrame Operations, User Input & Output, Average Calculation, File I/O, Data Visualization (Matplotlib and Seaborn)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./3. student_scores/students_scores_290625.csv')
print(df)
print("\n")

# F1: Calculate the average score for each student
df["Average"] = df[["Math", "English", "Science"]].mean(axis=1)
print(df[["Name", "Average"]])

# F2: Calculate the average score for each subject
subject_averages = df[["Math", "English", "Science"]].mean() # mean(axis=0) 是默认行为，表示对“每一列”求平均。
print("\nSubject Averages: \n", subject_averages)

# F3: Calculate the maximum score for each subject
subject_max = df[["Math", "English", "Science"]].max() # .max()	对列求最大值（axis=0）
print("\nSubject Maximums: \n", subject_max)

# F4: Identify students who failed in any subject
failing_students = df[df["Average"] < 60]
print("\nFailing Students:", failing_students[["Name", "Average"]])

# F5: Save the report to a CSV file
df.to_csv("./3. student_scores/score_report.csv", index=False)

# F6: Save the failing students to a separate CSV file
failing_students.to_csv("./3. student_scores/failing_students.csv", index=False)  

# F7: Visualize the average scores of students using a bar chart in matplotlib
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Average"], color="skyblue")
plt.title("Average Scores of Students")
plt.ylabel("Average Score")
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("./3. student_scores/average_score_bar_matplotlib.png")
plt.show()

# F8: Visualize the average scores of students using a bar chart in seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(x="Name", y="Average", data=df, palette="coolwarm")
plt.title("Average Scores of Students")
plt.ylabel("Average Score")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("./3. student_scores/average_score_bar_seaborn.png") 
plt.show()