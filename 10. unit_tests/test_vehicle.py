from unittest import TestCase, main

from vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(75, 300)

    def test_valid_initialization(self):
        self.assertEqual(self.vehicle.fuel, 75)
        self.assertEqual(self.vehicle.horse_power, 300)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_with_less_fuel_than_needed_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_with_enough_fuel_expect_reduce_fuel(self):
        self.vehicle.drive(10)

        self.assertEqual(self.vehicle.fuel, 62.5)

    def test_refuel_more_fuel_than_the_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel_with_less_fuel_than_the_capacity_expect_increase_fuel(self):
        self.vehicle.fuel = 10
        self.vehicle.refuel(10)

        self.assertEqual(self.vehicle.fuel, 20)

    def test_string_method_correct(self):
        result = self.vehicle.__str__()
        text = f"The vehicle has 300 " \
               f"horse power with 75 fuel left and 1.25 fuel consumption"

        self.assertEqual(result, text)


if __name__ == '__main__':
    main()
