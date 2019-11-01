# Importing the statistics module 
from statistics import mean

# beaking one line
break_one_line = "\n"

# Print 'hello world'
print("Hello World" + break_one_line)

# Print name
def print_name():
    name = "Stan"
    smily_emoji = ("\U0001f600")
    print(f"My name is {name}.")
    print(f"I am 20+ years of age. Young, right? {smily_emoji} {break_one_line}")
    # print("I am 20+ years of age. Young, right? " + ("\U0001f600") + break_one_line)

# printing the maximum element 
def max_num():
    num_list = [12, 4, 56, 17, 8, 99]
    print("The maximum number in this list: [12, 4, 56, 17, 8, 99] is ", max(num_list)) 

# Finding mean
def calc_mean():
    data_set = [12, 4, 56, 17, 8, 99]
    print("The mean: [12, 4, 56, 17, 8, 99] is % s" % (mean(data_set)))

# alphabets function
def alph():
    list = ["A for Apple", "B for Boy", "C for Cow", "...", "Z for Zebra"]
    for i in list:
        print(i)

# print all functions
print_name()
print(break_one_line)
max_num()
print(break_one_line)
calc_mean()
print(break_one_line)
alph()