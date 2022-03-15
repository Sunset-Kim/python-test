# 프린터큐
#3
#1 0
#5
#4 2
#1 2 3 4
#6 0
#1 1 9 1 1 1

test_case = int(input())

for _ in range(test_case):
  n, m =  list(map(int,input().split(' ')))
  queue = list(map(int,input().split(' ')))
  queue = [(i, idx) for idx, i in enumerate(queue)]
  print(queue)
  
  count = 0
  while True:
    if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
      count += 1
      if queue[0][1] == m:
        print(count)
        break
      else:
        queue.pop(0)
    else:
      queue.append(queue.pop(0))