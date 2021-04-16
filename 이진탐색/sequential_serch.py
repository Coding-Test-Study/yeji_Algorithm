# 순차 탐색

def serch(target):
    for i in range(n):
        if target==list[i]:
            return i+1

print("생성할 원소 갯수를 입력한 다음 한 칸 띄고 찾을 문장을 입력하세요")
n, target = input().split()
n=int(n)
print("앞서 적은 원소 개수만큼 문자열을 입력하세요 구분은 띄어쓰기 한 칸으로 합니다")
list=input().split()


print(serch(target))

"""
5 동빈
예지 한나 동빈 나영 화영
"""
