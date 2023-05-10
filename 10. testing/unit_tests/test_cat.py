from unittest import TestCase, main

from testing.cat import Cat


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat("Kudjo")

    def test_correct_initialization(self):
        self.assertEqual("Kudjo", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size, 0)

    def test_feeding_the_cat_after_if_was_fed_raise_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_if_cat_is_fed_after_eat(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_if_cat_is_sleepy_after_eat(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)

    def test_if_size_increase_by_one_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_if_cat_goes_to_sleep_while_hungry_raise_exception(self):
        self.cat.sleepy = True

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_cat_sleepy_expected_to_be_false_after_sleep(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
