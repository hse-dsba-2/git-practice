with open("grades.csv", "r") as file:
    for line in file:
        # print(line, end='')
        name = line.strip().split(",")[0]
        sum_grades = sum(map(int, line.strip().split(",")[1:]))
        # print(line.strip().split(',')[1:])
        print(name, sum_grades)
