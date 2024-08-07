
#!/usr/bin/env python3

'''
courses = [ 'uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635' ]
print(courses[0])
courses[0] = 'eac150'
print(courses[0])
print(courses)

courses.append('ops235')    # Add a new item to the end of the list object named courses
print(courses)

courses.insert(0, 'hwd101') # Add a new item to the specified index location, 
                            # the original item will be pushed to the next index location
print(courses)

courses.remove('ops335')    # Remove first occurrence of a matching item in the list object
print(courses)

sorted_courses = courses.copy() # Create a copy of the courses list
sorted_courses.sort()           # Sort the new list 
print(courses)
print(sorted_courses)


print()

list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]
length_of_list = len(list_of_numbers)    # Returns the length of the list
smallest_in_list = min(list_of_numbers)  # Returns the smallest value in the list
largest_in_list = max(list_of_numbers)   # Returns the largest value in the list

# Notice how the long line below is wrapped to fit on one screen:
print("List length is " + str(length_of_list) + 
      ", smallest element in the list is " + str(smallest_in_list) +
      ", largest element in the list is " + str(largest_in_list))



list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]
for item in list_of_numbers:
    print(item)


def square(num):
    return num * num

for value in list_of_numbers:
    print(square(value))
    '''

list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]

# Squares each item in a list of numbers, returns new list with squared numbers
def square_list(number_list):
    new_list = []
    for number in number_list:
        new_list.append(number * number)
    return new_list

new_list_of_numbers = square_list(list_of_numbers)
print(list_of_numbers)
print(new_list_of_numbers)