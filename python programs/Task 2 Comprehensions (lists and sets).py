# Given library codes for programming related books
library_codes = [14, 15, 16, 17, 18, 19, 20]

# Task 2A: Create a normal and comprehensive list that will display the codes.
normal_list = [code for code in library_codes]
print("Normal list of codes:", normal_list)

# Task 2B: Create a normal and comprehensive list that will add the codes together for auditing purpose.
sum_list = sum([code for code in library_codes])
print("Sum of all codes for auditing:", sum_list)

# Task 2C: Create a normal and comprehensive list that will display only codes that are tracked by odd numbers.
odd_list = [code for code in library_codes if code % 2 != 0]
print("Codes tracked by odd numbers:", odd_list)

# Task 2D: Create a set to display the list of codes.
codes_set = set(library_codes)
print("Set of codes:", codes_set)
