grades = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}


new_name = input("Enter a student name: ")
new_grade = int(input("Enter the grade for " + new_name + ": "))
grades[new_name] = new_grade

print("\nAll student grades:")
for name in grades:
    print(name + ": " + str(grades[name]))


total = 0
for score in grades.values():
    total += score

average = total / len(grades)
print("\nAverage grade:", round(average, 2))


highest = max(grades.values())
top_students = []
for name in grades:
    if grades[name] == highest:
        top_students.append(name)

print("Top grade:", highest, "by", ", ".join(top_students))
