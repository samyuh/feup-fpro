def sort_grades(records):
    def media(grades):
        grade = grades[2]
        final_grade = 0
        tests = len(grade)
        for i in range(tests):
            final_grade += int(grade[i])
        final_grade = final_grade/tests
        return final_grade

    records = sorted(records, key=lambda x: x[1])
    records = sorted(records, key=lambda x: x[0])
    records = tuple(sorted(records, key=lambda x: media(x), reverse = True))
    return records