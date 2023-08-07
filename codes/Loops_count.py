fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

while (1 < 2) :
    Loops_count = input("Loops count : ")
    if (Loops_count == "Q") :
        break
    else :
        Loop_fruit = fruits[:int(Loops_count)]
        fruit_print_format = "{0}. {1}"
        for (index, fruit) in enumerate(Loop_fruit, start=1) :
            print(fruit_print_format.format(index, fruit))
          
    

# Loops_count = int(input("Loops count : "))
# Loop_fruit = fruits[:Loops_count]
# fruit_print_format = "{0}. {1}"

# for (index, fruit) in enumerate(Loop_fruit) :
#     print(fruit_print_format.format(index, fruit))
#     if (Loops_count == "Q") :
#         break
