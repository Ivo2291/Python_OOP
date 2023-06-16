from unittest import TestCase, main

from car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Audi", "A-6", 12, 75)
        self.car.fuel_amount = 0

    def test_correct_initialization(self):
        self.assertEqual(self.car.make, "Audi")
        self.assertEqual(self.car.model, "A-6")
        self.assertEqual(self.car.fuel_consumption, 12)
        self.assertEqual(self.car.fuel_capacity, 75)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_no_value_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_model_no_value_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_equal_to_zero_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_below_zero_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -5

        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_below_zero_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -5

        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_capacity_equal_to_zero_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_below_zero_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5

        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_refuel_with_zero_or_negative_amount_of_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_with_more_fuel_then_fuel_capacity_expect_reduce_to_fuel_capacity_amount(self):
        self.car.refuel(self.car.fuel_capacity + 50)

        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    def test_drive_with_less_fuel_amount_than_needed_raise_exception(self):
        self.car.fuel_amount = 5

        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive_with_enough_fuel_for_the_distance_expect_reduce_fuel_amount(self):
        self.car.fuel_amount = self.car.fuel_capacity

        self.car.drive(200)

        self.assertEqual(self.car.fuel_amount, 51)


if __name__ == '__main__':
    main()
