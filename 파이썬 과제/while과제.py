import sys


i=0
while True:
    print("입력값을 넣어주세요")
    n = input()
    if n == "exit":
        sys.exit()
    n = int(n)
    i = i+1
    x = n * 2
    print(x)
    print(f"사용자가 입력한 문자는{n}입니다.")
    if i==5:
        print("숫자를 5회 이상 입력하셨습니다.")
        break













