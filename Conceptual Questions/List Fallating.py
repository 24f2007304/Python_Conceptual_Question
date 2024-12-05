# List Flattening: Write a function flatten_list(nested_list) that takes a nested list and returns a flattened version of the list.


# Example usage
# nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
# flat_list = flatten_list(nested_list)
# print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


# Can You find how it works
# Absolutely! Let's dive into how the recursive flatten_list function works step-by-step:

# Function: flatten_list
# python
''' Here in the isinstance we are going to the element is List or not'''
def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):  # Check if the element is a list
            flat_list.extend(flatten_list(element))  # Recursively flatten the sublist 
            ''' Here in the extend the flat_list untill the element is not got to append and there will huge Difference between append and extend it [flatten_list(element),12,23] and then flatten list became an elment by the help of function
            '''
        else:
            flat_list.append(element)  # If not a list, simply append the element
    return flat_list

print(flatten_list([12,34,[34,45,[34,45]]]))
# Step-by-Step Explanation:
# Initialize flat_list:
print(flatten_list([12,23,[23,34,[34,345,[45,4,57]]]]))
# Start with an empty list flat_list = [] to store the flattened elements.

# Iterate Over nested_list:

# Loop through each element in the input nested_list.

# Check if element is a List:

# Use isinstance(element, list) to check if the current element is a list.

# Recursive Call:

# If element is a list, call flatten_list(element) recursively to flatten this sublist.

# flat_list.extend(flatten_list(element)) adds all elements from the flattened sublist to flat_list.

# Append Non-List Elements:

# If element is not a list, simply append it to flat_list using flat_list.append(element).

# Return the flat_list:

# Once all elements have been processed, return the flat_list which now contains all the elements from the nested structure in a single, flat list.