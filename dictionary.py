# 초기화하기
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# len(thisdict)
# 3
# thisdict['model']
# 'Mustang'

# thisdict = {} : Empty
# thisdict = dict() : Empty

# ----- item
#  items는 enumerate와 비슷하게 작동, Key - value를 Tuple 형식으로
dict_format = "key : {0}, value : {1}"
for key, value in thisdict.items() :
    print(dict_format.format(key, value))
    pass

# dict_format = "key : {1}, value : {0}"
# for key, value in thisdict.items() :
#     print(dict_format.format(value, key))
#     pass

# ----- add / remove item in the dictionary
# thisdict["color"] = "Red" : key - value add, 같으면 update
# del thisdict["year"] : delete

pass