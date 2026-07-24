
number_1 = 1
number_2 = 2
pass


def print_msg() -> None:
    print('Welcome')
    print('message')
    # return
    # return None


print_msg()


def get_number_5() -> int:  # int float str list dict None
    print('function get_number_5 was called')
    number_5_to_give = 5
    return number_5_to_give


number_5 = get_number_5()
s = number_5 + 5
print(f'{number_5=}')


def foo():
    return


def calculate_summa(number_1: int | float, number_2: int | float) -> float:
    result = number_1 + number_2
    return result * 1.0


result_calculate_summa = calculate_summa(number_1=1, number_2=9.6)
print(result_calculate_summa)
mult = result_calculate_summa * 20
print(mult)



# ###############################

def get_distance(time_seconds: int | float, velocity_meters_per_second: int | float) -> float:
    distance = time_seconds * velocity_meters_per_second * 1.0
    distance = round(distance, 2)
    return distance


distance1 = get_distance(time_seconds=2, velocity_meters_per_second=2)
print(distance1)

distance2 = get_distance(time_seconds=2.522, velocity_meters_per_second=297.875765)
print(distance2)


