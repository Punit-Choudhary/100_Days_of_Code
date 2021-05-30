# Grading Program

"""
Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"

"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

def get_grade(score):
    if score > 90 and score <= 100:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectations"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    return grade

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    grade = get_grade(score)

    student_grades[student] = grade

print(student_grades)
