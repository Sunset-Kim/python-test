# 키로거
# 키보드를 누른 명령 모두를 기록한다.
# 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낸다
# 비밀번호창에서 입력한 키가 주어졌을때
# 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표

#입력
# 테스트 케이스의 갯수가 주어진다 (test_case)
# 테스트 케이스는 각 한줄, 입력한 순서대로 길이가 L인 문자열
# 백스페이스를 입력했다면 '-'
# 이때 커서 앞글자가 존재하면 지운다
# 화살표 입력은 < >
# 이때는 커서의 움직일 수 있다면
# 왼쪽 or 오른쪽으로 1씩 움직인다

# 2
# <<BP<A>>Cd-
# ThIsIsS3Cr3t
# ab<<-c

test_case = int(input())

for _ in range(test_case):
  left_stack = []
  right_stack = []
  data = input()
  
  for i in data:
    if i == '-':
      if left_stack:
        left_stack.pop()
    elif i == '<':
      if left_stack:
        right_stack.append(left_stack.pop())
    elif i == '>':
      if right_stack:
        left_stack.append(right_stack.pop())
    else:
      left_stack.append(i)
    
  left_stack.extend(reversed(right_stack))
  print(''.join(left_stack))


  
