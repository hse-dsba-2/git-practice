with open("grades.csv", "r") as file:
    all_grades = {}
    for line in file:
        sum_grades = line.strip().split(",")
        name = sum_grades[0]
        sum_grades = sum_grades[1:]
        sum_grades = sum(map(int, sum_grades))
        print(name, sum_grades)
        all_grades.update({name: sum_grades})
    grades_list = sorted(list(all_grades.values()))
    print('mean grade =', sum(grades_list) / len(grades_list))
    print('median grade =', grades_list[round(len(grades_list) / 2)] if len(grades_list) % 2 != 0 else (grades_list[
                                                                                                            round(
                                                                                                                len(grades_list) / 2)] +
                                                                                                        grades_list[
                                                                                                            round(
                                                                                                                len(grades_list) / 2) - 1]) / 2)
    names_greater_mean = list()
    names_less_median = list()
    for a, b in list(all_grades.items()):
        if b == grades_list[-1]:
            print(a, 'has max grade of', b)
        if b == grades_list[0]:
            print(a, 'has min grade of', b)
        if b > sum(grades_list) / len(grades_list):
            names_greater_mean.append(a)
        if b < (grades_list[round(len(grades_list) / 2)] if len(grades_list) % 2 != 0 else (grades_list[
                                                                                                round(
                                                                                                    len(grades_list) / 2)] +
                                                                                            grades_list[
                                                                                                round(
                                                                                                    len(grades_list) / 2) - 1]) / 2):
            names_less_median.append(a)
    print(*names_greater_mean, 'have grades greater than mean')
    print(*names_less_median, 'have grades less than median')
    # print(grades_list)

    # mean grade
    # median grade
    # max grade with name
    # min grade and name
    # names with greater grade than mean
    # name with less grade than median
