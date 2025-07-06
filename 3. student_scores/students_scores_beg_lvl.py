students_scores = {
    "Alice": {"Math": 85, "English": 90, "Science": 82},
    "Bob": {"Math": 88, "English": 92, "Science": 85},
    "Charlie": {"Math": 84, "English": 88, "Science": 80}   
}

# Function 1: calculate the average score for each student
for student, scores in students_scores.items():
    average = sum(scores.values()) / len(scores) # len(scores) 是scores 里 key 的数量。
    print(f"{student}'s average score is {average:.2f}")

# Function 2: calculate the average score for each subject
subject_totals = {}
subject_counts = {}

for scores in students_scores.values():
    for subject, score in scores.items():
        subject_totals[subject] = subject_totals.get(subject, 0) + score
        subject_counts[subject] = subject_counts.get(subject, 0) + 1
# subject_totals = {
#     "Math": 257,
#     "English": 264,
#     "Science": 247
# }
# subject_counts = {
#     "Math": 3,
#     "English": 3,
#     "Science": 3
# }

for subject in subject_totals:
    average = subject_totals[subject] / subject_counts[subject]
    print(f"{subject}'s average score is {average:.2f}")
