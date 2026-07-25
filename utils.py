def get_travel_info(driver: str, passenger_1: str = "", passenger_2: str = "", passenger_3: str = 'sister') -> str:
    passengers = [passenger_1, passenger_2, passenger_3]
    #                  ['Anastasiia', '', '']  - result of this ^
    real_passengers = []
    for passenger in passengers:
        if passenger:
            real_passengers.append(passenger)

    passengers_str = ", ".join(real_passengers)
    print(passengers_str)

    people_in_car = f"DRIVER: {driver.title()}, passengers: {passengers_str}."
    return people_in_car