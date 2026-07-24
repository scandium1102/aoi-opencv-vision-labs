import unittest

from labs.focus_error_signal import detector_sweep, mean_axis_difference
from labs.thin_lens import image_distance


class OpticsLabTests(unittest.TestCase):
    def test_thin_lens_equation(self):
        self.assertAlmostEqual(image_distance(100.0, 50.0), 100.0)

    def test_focus_sweep_is_finite(self):
        distances, errors = detector_sweep()
        self.assertEqual(len(distances), len(errors))
        self.assertGreater(mean_axis_difference(100.0), 0.0)


if __name__ == "__main__":
    unittest.main()
