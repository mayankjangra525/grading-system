def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

score = float(input("Enter the student's score (0-100): "))
if 0 <= score <= 100:
    print("Grade:", get_grade(score))
else:
    print("Error: Score must be between 0 and 100.")
