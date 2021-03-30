def cal_dist(num, now_l, now_r, pos, handed):
  X, Y = 0, 1
  dist_l, dist_r = (abs(pos[now][X] - pos[num][X]) + abs(pos[now][Y] - pos[num][Y]) for now in [now_l, now_r])
  # 거리가 같으면
  if dist_l == dist_r :
    return 'R' if handed == 'right' else 'L'
  return 'R' if dist_l > dist_r else 'L'


def solution(numbers, hand):
  # 왼손잡이인지, 오른손 잡이인지
  HANDED = hand
  # 번호 좌표화
  position = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)}
  
  # 왼쪽 숫자, 오른쪽 숫자
  left, right = set([1,4,7]), set([3,6,9])
  # 손 위치 초기화
  now_l, now_r = '*', '#'
  # solution
  answer = ''
  for num in numbers:
    if num in left:
      answer += 'L'
      now_l = num
    elif num in right:
      answer += 'R'
      now_r = num
    else:
      answer += cal_dist(num, now_l, now_r, position, HANDED)
      if answer[-1] == 'L':
        now_l = num
      else:
        now_r = num
    return answer
