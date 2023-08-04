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


# ------------------- 자바의 ;, {}, 변수의 datatype 규칙과 달리 Python은 tab만 주의
thislist = ["apple", "banana", "cherry"]

# thislist.append("melon") : 새로운 아이템을 뒤에 추가
# thislist.pop() : 끝에 있는 아이템이 삭제

pass

# thislist = []
# thislist = list () : 리스트 초기화, 실무에서는 이 방식이 더 활용

# x = str("s1") : casting e.g. int, float, string, etc.


