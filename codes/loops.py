thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# for item in items:
#     pass

for fruit in thislist:
    print(fruit)
pass

# range(2, 10)
# for(int i = 0; i < 10; i ++) {} : 아래 구문을 자바로 작성할 시

for i in range(2, 10):
    print(i)

pass

# while
# while () :
# pass

first = 3
while (first < 6) :
    pass
    print("while count {}".format(first))
    first = first + 1


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits_enumerate = enumerate(fruits)

# next(fruits_enumerate)
# (1, 'banana') : 이와 같은 형식을 Tuple이라고 함 : 한 번 세팅되면 변화하지 않음
# 데이터묶음

# --- Tuple 묶음
for index_fruit in fruits_enumerate :
    print(index_fruit)
    pass

# --- Tuple 분리

fruit_print_format = "number: {0}, fruit name: {1}"

for (index, fruit) in fruits_enumerate :
    print(fruit_print_format.format(index, fruit))
    pass
pass