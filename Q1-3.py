user_input_number1 = input()
user_input_number2 = input()
user_input_number3 = input()

number_list = []
number_list.insert(0,int(user_input_number1))
number_list.insert(1,int(user_input_number2))
number_list.insert(2,int(user_input_number3))
sorted_number_list = sorted(number_list,reverse=True)

print(sorted_number_list)

# これが解答

# number_list = []
#
# user_input_number = input()
# number_list.insert(0,int(user_input_number))
#
# user_input_number = input()
# number_list.insert(0,int(user_input_number))
#
# user_input_number = input()
# number_list.insert(0,int(user_input_number))
#
# sorted_number_list = sorted(number_list,reverse=True)
#
# print(sorted_number_list)

