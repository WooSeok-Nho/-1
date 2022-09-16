score = int(input())


def get_grade(score):
    if score > 90:
        print("A")
        return
    elif score > 80:
        print("B")
        return
    elif score > 70:
        print("C")
        return
    else:
        print("F")
        return


grade = get_grade(score)
print(grade)
