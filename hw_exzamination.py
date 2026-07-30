# def average(a, b, c):
#
# Вимоги:
#
# приймає 3 числа
# повертає середнє значення
# округлення до 2 знаків

def get_average(number_1: float | int, number_2: float | int, number_3: float | int) -> float:
    arguments_count = 3
    average_result = (number_1 + number_2 + number_3) / arguments_count
    return round(average_result, 2)


average = get_average(66, 6.6, 0)