class Area():
    def Area_cal(self, cal):
        self.cal = cal
        Horizon = int(input('가로값을 입력하세요'))
        Vertical = int(input('세로값을 입력하세요'))
        Square.cal = Horizon * Vertical
        triangle.cal = Horizon * Vertical //2
        circle.cal = Horizon//2 * Horizon //2 * 3.14

Square = Area()
triangle = Area()
circle = Area()

print("사각형의 넓이를 구하기 위해")
Square.Area_cal("cal")
print("삼각형의 넓이를 구하기 위해")
triangle.Area_cal("cal")
print("원의 넓이를 구하기 위해")
circle.Area_cal("cal")

print(f'사각형의 넓이는 :{Square.cal}입니다.')
print(f'삼각형의 넓이는 :{triangle.cal}입니다.')
print(f'원의 넓이는 :{circle.cal}입니다.')



