# Python Comprehension
# - 다른 Sequence 로 부터 새로운 Sequence (lterable Object)를 만들수 있는 기능

# 예제 1 종류가 다른 데이터에서 정수 or string만 가지고 오기
dataset = [4, True, 'Dave', 2.1, 3]
int_data = [num for num in dataset if type(num) == int]
int_float_data = [num for num in dataset if type(num) == int or type(num) == float]
# print(int_data, int_float_data)

# 예제 2 계산된 결과를 반환하는 데이터셋 만들기
int_square_lit = [num*num for num in dataset if type(num)==int]
# print(int_square_list)

# 예제 3 자료구조 set으로 comprehension
int_square_set = {num * num for num in dataset if type(num) == int and num > 3}
# print(int_square_set)

#  dictionary comprehension
# 예제 4 아이디가 2이상인 데이터를 이름 : 아이디 형식으로 변환
id_name = {1: "First",2: "Second", 3: "Third"}

name_id = {value:key for key,value in id_name.items() if key >= 2}
print(name_id)


# list = [i for i in range(101)]