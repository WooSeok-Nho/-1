class Cal():
    def set_data(self, first, second):
        self.first = first
        self.second = second
    def plus(self):
        result = self.first + self.second
        return result
    def minus(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
try:
    calc = Cal()
    calc.set_data(v,0)


    print(calc.plus())
    print(calc.minus())
    print(calc.mul())
    print(calc.div())
except ValueError:
    print("입력값 이 숫자가 아닙니다.")
except ZeroDivisionError:
    print("0으로는 나눌수 없습니다.")
except NameError:
    print("입력값 이 숫자가 아닙니다.")

