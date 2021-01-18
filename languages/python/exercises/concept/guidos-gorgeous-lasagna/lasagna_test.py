import unittest
from lasagna import EXPECTED_BAKE_TIME, bake_time_remaining, preparation_time_in_minutes, elapsed_time_in_minutes


class LasagnaTest(unittest.TestCase):

    def test_EXPECTED_BAKE_TIME(self):
        self.assertEqual(EXPECTED_BAKE_TIME, 40)


    def test_bake_time_remaining(self):
        input_data = [1, 2, 5, 10, 15, 23, 33, 39]
        result_data = [40 - item for item in input_data]

        for variant, time, result in zip(range(1, len(input_data)+1), input_data, result_data):
            with self.subTest(f"variation #{variant}", time=time, result=result):
                self.assertEqual(bake_time_remaining(time), result, msg=f'Expected: {result} but the bake time remaining was calculated incorrectly.')


    def test_preparation_time_in_minutes(self):
        input_data = [1, 2, 5, 8, 11, 15]
        result_data = [item * 2 for item in input_data]

        for layers, time in zip(input_data, result_data):
            with self.subTest("preparation time calculation variants", layers=layers, time=time):
                self.assertEqual(preparation_time_in_minutes(layers), time)


    def test_elapsed_time_in_minutes(self):
        prep_time_data = (1, 2, 5, 8, 11, 15)
        elapsed_time_data = (3, 7, 8, 4, 15, 20)
        result_data = [prep * 2 + elapsed for prep, elapsed in zip(prep_time_data, elapsed_time_data)]

        for layers, time, total_time in zip(prep_time_data, elapsed_time_data, result_data):
            with self.subTest("elapsed time remaining variants", layers=layers, time=time, total_time=total_time):
                self.assertEqual(elapsed_time_in_minutes(layers, time), total_time)


    def test_docstrings(self):
        self.assertIsNotNone(elapsed_time_in_minutes.__doc__)
        self.assertIsNotNone(preparation_time_in_minutes.__doc__)
        self.assertIsNotNone(elapsed_time_in_minutes.__doc__)


if __name__ == "__main__":
    unittest.main()
