# Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

print ("Printing current and previous number sum in a range(10)")
previous_number = 0

#creating funtions
for i in range (0,10):
    current_number = i
    sum = current_number + previous_number

    #printing result
    print ("Current Number: ", current_number, "Previous Number: ", previous_number, "Sum: ", sum)

    previous_number = i


