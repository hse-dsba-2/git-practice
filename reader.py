with open("grades.csv", "r") as file:
    for line in file:
        sum_grades = line.strip().split(",")
        name = sum_grades[0]
        sum_grades = sum_grades[1:]
        sum_grades = sum(map(int, sum_grades))
        print(name, sum_grades)