from prac_09.unreliable_car import UnreliableCar
def main():
    """Test UnreliableCars."""
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    print(f"Attempting to drive {good_car.name} and {bad_car.name} several times...")
    for i in range(1, 12):
        print(f"Attempt {i}:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")
        print("-" * 25)
        print("Final state of the cars:")
        print(good_car)
        print(bad_car)


main()