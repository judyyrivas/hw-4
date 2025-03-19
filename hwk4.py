# Programmers: Judy Rivas
# Course:  CS151, Eric Ebert
# Due Date: 03/19/25
# Programming Assignment: HWK 4
# Problem Statement: Created functions, sentinel loops and lists for previous class notes
# Data In: Test scores
# Data Out: Welcome message. Test score average. List of scores entered.
# Credits: Class Notes 18, 19 and 20.

# Welcome Statement/Purpose
print("Welcome to your grade calculator! This program will give you the average of your entered test scores.")

# Purpose: Main function that sets values for count, total and sentinel
# Parameters: None
# Return: None
def main():
    count = 0 # Counter for number of scores entered
    total = 0 # Sum of all test scores
    SENTINEL = -999 # Sentinel value to stop program
    grade_list = [] # List to store test scores

    # Purpose: Function that gets users test scores, calculates the average, and outputs the average and list of test scores
    # Parameters: Count and total
    # Return: Returns count, total and grade list
    def get_testscores(count, total):
        # Get users test scores
        score = int(input("Give a test score (-999 to end): "))

        # Control loop to collect test scores until sentinel value is entered
        while score != SENTINEL:
            grade_list.append(score) # Store the score in the list
            total += score # Add the score to the total sum
            count += 1 # Increase the count of scores entered
            score = int(input("Give a test score (-999 to end): "))

        # Return collected date
        return count, total

    # Get the total count and sum of scores
    count, total = get_testscores(count, total)

    # Calculate and display the average of the scores entered
    if count > 0:
        average = total / count
        print("The average score is:", int(average))
    else:
        print("No scores entered.")

    # Return list of scores
    return grade_list

# Call the function
grades = main()
print("Grades entered:", grades)



