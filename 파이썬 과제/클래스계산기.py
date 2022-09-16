class Calc():
    def cal_result(self, result):
        self.result = result

        fnumber = int(input())
        snumber = int(input())
        Plus.result = fnumber + snumber
        Minus.result = fnumber - snumber
        multiplication.result = fnumber * snumber
        Division.result = fnumber // snumber

Plus = Calc()
Minus = Calc()
multiplication = Calc()
Division = Calc()

print("연산할 숫자를 차례 대로 입력 하세요")
print("덧셈을 할 숫자를 입력 하세요")
Plus.cal_result("result")
print("뺄셈을 할 숫자를 입력 하세요")
Minus.cal_result("result")
print("곱셈을 할 숫자를 입력 하세요")
multiplication.cal_result("result")
print("나눗셈 을 할 숫자를 입력 하세요")
Division.cal_result("result")

print(f"덧셈의 결과는 :{Plus.result}입니다.")
print(f"뺄셈의 결과는 :{Minus.result}입니다.")
print(f"곱셈의 결과는 :{multiplication.result}입니다.")
print(f"나눗셈 의 결과는:{Division.result}입니다.")




