# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# pseudocode


# Initialize the previous number to 0 
# loop from 1 to 10
# calculate and print the sum of current and previous numbers


# --------------------------- actual code ---------------------------------
# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 20 numbers, and in each iteration, print the sum of the current and previous number.

# Initialize the previous number to 0 
previous_num = 0

# loop from 1 to 20
for i in range(1, 21):
    # calculate and print the sum of current and previous numbers
    current_sum = previous_num + i
    
    # Print the sum of the current and previous numbers
    print(f"Current Number: {i}, Previous Number: {previous_num}, Sum: {current_sum}")
    

