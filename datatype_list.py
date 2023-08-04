thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
pass

# check datatype
# type(thislist)
# <class 'list'>

# len(thislist)  => 순열방식에서 작동 e.g. list, string, etc
# 7

# thislist[1:3] => -1을 해서 1, 2만 나옴
# ['banana', 'cherry']

# thislist[:-1]
# ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']

#  ---------

thislist[1] = "watermelon"
pass

# thislist[1:3] = ["cherry", "watermelon"] => 둘의 순서를 바꿈
# thislist.sort() => 아이템 정렬, quick sort
# thislist.sort(reverse=True) => descending 정렬, 이때 T 대문자 주의
