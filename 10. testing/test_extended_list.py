from unittest import TestCase, main

from testing.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer_list = IntegerList(1, 'opa', 2, 3.14, 3, '100')

    def test_correct_initialization(self):
        self.assertEqual(self.integer_list._IntegerList__data, [1, 2, 3])

    def test_get_data_correct(self):
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3])

    def test_add_non_integer_element_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add('opa')

        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_add_integer_element(self):
        result = self.integer_list.add(13)

        self.assertEqual(self.integer_list._IntegerList__data, [1, 2, 3, 13])
        self.assertEqual(result, [1, 2, 3, 13])

    def test_remove_invalid_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(10)

        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_remove_valid_index(self):
        result = self.integer_list.remove_index(2)

        self.assertEqual(result, 3)
        self.assertEqual(self.integer_list._IntegerList__data, [1, 2])

    def test_get_invalid_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(10)

        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_get_with_valid_index(self):
        result = self.integer_list.get(1)

        self.assertEqual(result, 2)

    def test_insert_element_on_invalid_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(5, 10)

        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_insert_non_integer_element_raise_Value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(2, 'opa')

        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_insert_valid_element_and_index(self):
        self.integer_list.insert(2, 10)

        self.assertEqual(self.integer_list._IntegerList__data, [1, 2, 10, 3])

    def test_get_biggest_number_correct(self):
        result = self.integer_list.get_biggest()

        self.assertEqual(result, 3)

    def test_get_index_correct(self):

        self.assertEqual(self.integer_list.get_index(3), 2)


if __name__ == '__main__':
    main()
