# 곱하기 혹은 더하기를 하여 최대 숫자 도출하기

# 답안
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
  # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num
  
print(result)

''' # 내가 푼 방법
s = input("숫자를 입력하세요 ")
result = 0 # 결과값
bf = 0 # 이전 숫자

for i in s: #문자열 하나씩 반복
  if (bf+int(i)) >= bf*int(i): # 더하기가 곱하기보다 크거나 같으면 숫자를 결과값에 더하기 
    result += int(i)
  else: # 이외에는 숫자를 결과값에 곱하기
    result *= int(i) 
  bf = int(i) # 앞의 숫자 bf

print(result)
'''
