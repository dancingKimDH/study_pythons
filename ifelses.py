first = 3
second = 4

# if - elif - else

if (first < second) :
    print("less first")
elif (first == second) :
    print("equal")
else :
    print("greater second")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# if 문에는 break가 동작하지 않음. 따라서 for에만 작동!
# 이중 if문에서도 for에만 적용
# 자료구조 가운데 stack과 연관되어 있음

for fruit in thislist:
    pass
    if (fruit == "orange") :
        break
    print(fruit)