# 모험가 길드
# <답안>
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포돌를 낮은 것부터 하나씩 확인하며
  count += 1 # 현재 그룹에 해당 모험가를 포함시키기
  if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    result += 1
    count = 0
print(result)


'''
# <내풀이>
n = int(input())
x = list(map(int, input().split()))
group = 0
x.sort() #오름차순 정렬

while True:
  # 공포도 x인 모험가가 x명이상 있는경우 x명끼리 그룹 1개 추가
  if x.count(x[0]) >= x[0]: 
    group+=1
    for _ in range(x[0]): # 공포도 x인 모험가 x명 x리스트에서 제외
      del x[0]
  else: # if 조건문에 해당하지 않을 시 그룹 참여 제한
    del x[0]

  if len(x) == 0: # 더이상 그룹을 만들 수 없을 때 종료
    break

print(group) # 모험가 그룹 수 출력
'''
