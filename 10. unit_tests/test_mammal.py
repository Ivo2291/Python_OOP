from unittest import TestCase, main

from mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Deks", "dog", "bau - bau")

    def test_correct_initialization(self):
        self.assertEqual(self.mammal.name, "Deks")
        self.assertEqual(self.mammal.type, "dog")
        self.assertEqual(self.mammal.sound, "bau - bau")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound_expect_to_return_name_and_sound(self):

        self.assertEqual(self.mammal.make_sound(), f"Deks makes bau - bau")

    def test_get_kingdom_expect_to_return_animal_kingdom(self):

        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info_expect_to_return_animal_name_and_animal_type(self):

        self.assertEqual(self.mammal.info(), f"Deks is of type dog")


if __name__ == '__main__':
    main()
