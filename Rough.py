" Here we have take a input from user and also number of number from in a line"
"For Example :"
"5"
"12346"


n = int(input())
while True:
    user_input =input("Enter The Number as you Want")
    if len(user_input)>n or len(user_input)<n:
          print(f'Invalid Numbers')
   
    l =[]
    for i in user_input:
        l.append(i)
    max = max(l)
    newl =l.remove(max)
    print(newl)
print(get_n_words_in_a_line(3)) 
# def get_n_words_in_a_line(n):
#     while True:
#         user_input = input(f"Enter exactly {n} words separated by spaces: ").strip()
#         words = user_input.split()
#         if len(words) == n:
#             return words
#         else:
#             print(f"Invalid input. Please enter exactly {n} words.")

# # Example usage
# n = int(input("Enter the number of words allowed: "))
# words = get_n_words_in_a_line(n)
# print(f"You entered: {words}")

# # Process each word with a for loop
