'''
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N에서 K로 나눈다.

예를 들어 N이 17, K가 4라고 가정하자. 이때 1번의 과정을 한 번 수행하면 N은 16이다. 이후에 2번의 과정을 수행하면 N이 1이 된다. 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 된다. 이는 N을 1로 만드는 최소 횟수이다. 

N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.
'''

n,k = map(int, input().split())
result = 0

while True:
  # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
  target = (n//k) * k
  result += (n - target)
  n = target
  # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
  if n<k:
    break
  # K로 나누기
  result += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)



'''
# 단순한 코드
n,k = map(int, input().split())
cnt = 0 # 수행해야 하는 횟수

while n>1: # n이 1일때까지 반복
  if n%k==0:
    cnt+=1
    n=n//k
  else:
    n-=1
    cnt+=1

print(cnt)
'''

