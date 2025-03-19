

print("Welcome to your grade calculator! This program will give you the average of your entered test scores.")
def main():
    count = 0
    total = 0
    SENTINEL = -999
    grade_list = []

    def get_testscores(count, total):
        score = int(input("Give a test score (-999 to end): "))

        while score != SENTINEL:
            grade_list.append(score)
            total += score
            count += 1
            score = int(input("Give a test score (-999 to end): "))

        return count, total

    count, total = get_testscores(count, total)

    if count > 0:
        average = total / count
        print("The average score is:", int(average))
    else:
        print("No scores entered.")

    return grade_list

grades = main()
print("Grades entered:", grades)



