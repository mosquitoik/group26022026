from utils import get_travel_info


message3004 = get_travel_info(driver='Alla', passenger_1='Andriy', passenger_2='Pavlo', passenger_3='Vasyl')
print(message3004)


message0105 = get_travel_info(driver='Vasyl', passenger_3='Alla', passenger_2='Andriy')
print(message0105)


message0105 = get_travel_info('Vasyl', 'Alla', passenger_3='Pavlo', passenger_2='Petro')
print(message0105)
message0105 = get_travel_info('Vasyl', 'Alla', passenger_3='Petro')
print(message0105)


message0105 = get_travel_info('Vasyl', passenger_3='Petro')
print(message0105)


driver, passenger_1,  *other = 'Vasyl', 'Alla', 'Pavlo', 'Petro'
print(driver)
print(passenger_1)
print(other)



message3004 = get_travel_info(driver='Alla', passenger_1='Andriy', passenger_2='Pavlo', passenger_3='Vasyl')
print(message3004)


people = {
    "passenger_1": 'Nicole',
    "passenger_2": 'Nicole2',
    "driver": 'Ivan',
}

new_way_arguments_provided = get_travel_info(**people)
print(new_way_arguments_provided)


# TEMPLATE_STR = 'Our driver today is {} and passenger {passenger_1}'
# msg = TEMPLATE_STR.format(*other)
# print(msg)

TEMPLATE_STR = 'Our driver today is {driver} and passenger {passenger_1}'
msg = TEMPLATE_STR.format(**people)
print(msg)



test_func = get_travel_info('Vadym', "Anastasiia")
print(test_func)