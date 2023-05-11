import unittest
from testing.worker import Worker


class TestWorker(unittest.TestCase):

    def setUp(self):
        self.worker = Worker("Ivo", 1000, 100)

    def test_valid_initialization_on_worker(self):
        self.assertEqual("Ivo", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_below_or_equal_to_zero_when_working_raise_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_money_increase_when_working(self):
        self.worker.work()

        self.assertEqual(self.worker.salary, self.worker.money)

    def test_worker_energy_decrease_when_working(self):
        self.worker.work()

        self.assertEqual(99, self.worker.energy)

    def test_worker_energy_increase_when_resting(self):
        self.worker.rest()

        self.assertEqual(101, self.worker.energy)

    def test_get_correct_info(self):
        self.assertEqual('Ivo has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    unittest.main()
