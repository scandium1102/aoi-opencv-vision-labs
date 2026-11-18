import unittest

from labs.coursework_focus import best_distance, mean_axis_difference


class CourseworkFocusTests(unittest.TestCase):
    def test_detector_sweep_matches_coursework(self):
        distance, error = best_distance()
        self.assertAlmostEqual(distance, 100.0375939849624)
        self.assertAlmostEqual(error, 0.00104, places=5)

    def test_axial_offset_series_matches_coursework(self):
        distance, _ = best_distance()
        expected = [15.0056, 10.0038, 5.00188, 0.00104, 5.00188, 10.0038, 15.0056]
        for offset, recorded in zip(range(-30, 31, 10), expected):
            with self.subTest(offset=offset):
                self.assertAlmostEqual(mean_axis_difference(distance, offset), recorded, delta=0.00006)


if __name__ == "__main__":
    unittest.main()
