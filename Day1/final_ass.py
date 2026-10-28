def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


def classify_grade(score):
    if score >= 80:
        return "A"  
    elif score >= 60:
        return "B"  
    elif score >= 50:
        return "C"   
    else:
        return "FAIL"  


def count_passed(students):
    count = 0
    for student in students:
        if student["score"] >= 50:
            count += 1
    return count


def main():
    students = [] 

    print("=== Enter Student Information (At least 5 students) ===\n")


    for i in range(1, 5):
        print(f"Enter details for Student ({i}):")
        name = input("Name: ")
        age = int(input("Age: "))
        study_hours = float(input("Study Hours: "))


        while True:
            score = float(input("Python Score (0-100): "))
            if 0 <= score <= 100:
                break
            print("Error: Score must be between 0 and 100. Please try again.")


        student_data = {
            "name": name,
            "age": age,
            "study_hours": study_hours,
            "score": score,
        }
        students.append(student_data)
        print("-" * 30)


    print("\n==========================================")
    print("      STUDENT PERFORMANCE REPORT          ")
    print("==========================================")

    scores = []

    for student in students:
        grade = classify_grade(student["score"])
        scores.append(student["score"])
        print(
            f"Name: {student['name']} | Age: {student['age']} | "
            f"Study Hours: {student['study_hours']} hrs | Score: {student['score']} | Grade: {grade}"
        )

    avg_score = calculate_average(scores)
    passed_count = count_passed(students)

    print("\n------------------------------------------")
    print(f"Average Score           : {avg_score:.2f}")
    print(f"Passing Students Count  : {passed_count} / {len(students)}")
    print("==========================================")


main()