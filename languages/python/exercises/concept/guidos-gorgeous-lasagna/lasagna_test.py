import unittest
from lasagna import EXPECTED_BAKE_TIME, bake_time_remaining, preparation_time_in_minutes, elapsed_time_in_minutes


class LasagnaTest(unittest.TestCase):

    def test_EXPECTED_BAKE_TIME(self):
        self.assertEqual(EXPECTED_BAKE_TIME, 40, msg="Expected a constant of EXPECTED_BAKE_TIME with a value of 40.")


    def test_bake_time_remaining(self):
        input_data = [1, 2, 5, 10, 15, 23, 33, 39]
        result_data = [40 - item for item in input_data]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, time, result in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", time=time, result=result):
                self.assertEqual(bake_time_remaining(time), result,
                                 msg=f'Expected: {result} but the bake time remaining was calculated incorrectly.')


    def test_preparation_time_in_minutes(self):
        input_data = [1, 2, 5, 8, 11, 15]
        result_data = [item * 2 for item in input_data]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, layers, time in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", layers=layers, time=time):
                self.assertEqual(preparation_time_in_minutes(layers), time,
                                 msg=f'Expected: {time} minutes, but preparation time'
                                     f' was calculated incorrectly.')


    def test_elapsed_time_in_minutes(self):
        prep_time_data = (1, 2, 5, 8, 11, 15)
        elapsed_time_data = (3, 7, 8, 4, 15, 20)
        result_data = [prep * 2 + elapsed for prep, elapsed in zip(prep_time_data, elapsed_time_data)]
        number_of_variants = range(1, len(prep_time_data) + 1)

        for variant, layers, time, total_time in zip(number_of_variants, prep_time_data, elapsed_time_data, result_data):
            with self.subTest(f"variation #{variant}", layers=layers, time=time, total_time=total_time):
                self.assertEqual(elapsed_time_in_minutes(layers, time), total_time,
                                 msg=f'Expected: {time} minutes elapsed, but the timing'
                                     f' was calculated incorrectly.')


    def test_docstrings(self):
        #input_data = [elapsed_time_in_minutes, preparation_time_in_minutes, bake_time_remaining]
        #number_of_variants = range(1, len(input_data) + 1)

        #for variant, docstring in zip(number_of_variants, input_data):
        #    with self.subTest(f"variation #{variant},", docstring=docstring):
        #        self.assertIsNotNone(docstring.__doc__, msg=f"Expected a docstring for {docstring.__name__}, but no docstring was found.")
        self.assertIsNotNone(elapsed_time_in_minutes.__doc__, msg="Expected a docstring for elapsed_time_in_minutes, but no docstring was found.")
        self.assertIsNotNone(preparation_time_in_minutes.__doc__, msg="Expected a docstring for preparation_time_in_minutes, but no docstring was found.")
        self.assertIsNotNone(bake_time_remaining.__doc__, msg="Expected a docstring for bake_time_remaining, but no docstring was found.")


if __name__ == "__main__":
    unittest.main()
