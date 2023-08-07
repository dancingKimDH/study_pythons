# package == module(python)

# how to define a function
def function_name ():
    pass
    return 0

# call the function
# 은폐 : 안의 내용은 정확히 알 수 없음 : 4번 라인 다음으로 10번 라인으로 이동, 다시 위로
function_name()
pass

# print(function_name())
# 0

# deliver (평범한) params to a function
def add (first, second):
    sum = first + second
    return sum

result_sum = add(4, 6)
pass

# set default value with params
def minus(first, second=0):
    result = first - second
    return result

minus(3, 5)
minus(3)