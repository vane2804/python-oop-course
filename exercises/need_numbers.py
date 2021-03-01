# Input: A single string
# Output: 2 numbers.
#     - The total sum of the values
#     - The average
# Constraints:
    # - The separator character is a blank space
    # - The format of each grade is: "subject name","equal symbol","grade value". (English=68)
# Edge Cases:
#     - Grade is negative


# - Split the string using the blank space.
# - Count the number of elements in the list
# - Split each string using the equal symbol
# - Get the value that is after the equal symbol
# - Cast the value to a number
# - Get the sum
# - Get the average

input = "English=68 Logic=75 Uml=87 Code=80"

subject_list =  input.split()
list_count = len(subject_list)
print("There are [{}] subjects".format(list_count))

grade_list = []
sum_value = 0

for subject in subject_list:
    grade = float(subject.split("=")[1])
    sum_value = grade + sum_value

average_value = sum_value / list_count

print("The total value is: [{}]".format(sum_value))
print("The average value is: [{}]".format(average_value))

