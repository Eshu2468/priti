# # import base64

# # mounika = "RHVyZ2Fzb2Z0QDEyMzQ1"
# # akash = base64.b64decode(mounika)   #converts strings into bytes
# # bhavani = akash.decode("UTF-8")   #converts bytes to readable string
# # print(f"decoded string: {bhavani}")
# # print(f"decoded string: {akash}")


# # from day9 import calculated_discounts as cd


# # print(cd)



# # Define the function to filter
# def custom_filter_function(element):
#     # Add your condition here
#     return element % 2 == 0  # Example: filter even numbers

# # Define a sequence (list, tuple, etc.)
# sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Use filter() to apply the filter function
# filtered_sequence = filter(custom_filter_function, sequence)

# # Convert the filter object to a list (or other iterable)
# filtered_list = list(filtered_sequence)

# # Print the result
# print(filtered_list)



# Define the filter function for strings
def custom_string_filter(s):
    # Example condition: filter strings that contain the letter 'a'
    return 'a' in s.lower()

# Define the list of strings
string_list = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape"]

# Apply the filter
filtered_strings = filter(custom_string_filter, string_list)

# Convert to list and print the result
filtered_list = list(filtered_strings)
print(filtered_list)
print(filtered_strings)
