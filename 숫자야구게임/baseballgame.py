from random import randint
import time
from datetime import datetime
import sys

print("게임에서 입력받을 자릿수를 정해주세요")

Str = input()
if Str.isdigit():  ## isdigit 앞에 있는 변수 내용이 정수일경우 true이고 문자일경우 false가 된다.
    Pnum = int(Str)
elif Str == "exit":
    sys.exit(0)

start_time = time.time()

def PC_numbers():
    Pnumbers = []
    i = 0
    new_number = 0
    while i < Pnum:
        new_number = randint(0, 9)
        if new_number not in Pnumbers:
            Pnumbers.append(new_number)
            i += 1
    return Pnumbers


def take_mynumber():
    print(f"숫자 {Pnum}개를 하나씩 차례대로 입력하세요.")
    i = 0
    mynumber = []
    while i < Pnum:

        gue_number = input("{}번째 숫자를 입력하세요: ".format(i + 1))
        if gue_number.isdigit():
            gue_number = int(gue_number)
        elif gue_number == "exit":
            sys.exit(0)

        if gue_number > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        if gue_number in mynumber:
            print("중복되는 숫자입니다. 다시 입력하세요. ")
        else:
            mynumber.append(gue_number)
            i += 1

    return mynumber


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0
    i = 0

    while i < len(guess):

        if guess[i] == solution[i]:
            strike_count += 1
            i += 1
        elif guess[i] in solution:
            ball_count += 1
            i += 1
        else:
            i += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = PC_numbers()
tries = 0

while 1:
    GUESS = take_mynumber()
    strike, ball = get_score(GUESS, ANSWER)

    print("{}S {}B ".format(strike, ball))
    tries +=1

    if strike == Pnum:
        break

end_time = time.time()
print(f"정답입니다. {tries}번 만에 결과를 맞추셨습니다. 정답까지 걸린 시간 : {end_time - start_time:.5f}초입니다."
      f"현재 시각은 :{datetime.now()}입니다.")






