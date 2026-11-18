import unittest

from labs.focus_error_signal import detector_sweep, mean_axis_difference
from labs.sharpness import demo_images, focus_scores
from labs.thin_lens import image_distance


class OpticsLabTests(unittest.TestCase):
    def test_thin_lens_equation(self):
        self.assertAlmostEqual(image_distance(100.0, 50.0), 100.0)

    def test_focus_sweep_is_finite(self):
        distances, errors = detector_sweep()
        self.assertEqual(len(distances), len(errors))
        self.assertGreater(mean_axis_difference(100.0), 0.0)

    def test_astigmatic_balance_between_focal_planes(self):
        fx, fy = 100.0, 120.0
        balance = 2 * fx * fy / (fx + fy)
        self.assertAlmostEqual(mean_axis_difference(balance), 0.0)
        distances, errors = detector_sweep()
        self.assertAlmostEqual(distances[errors.argmin()], balance, delta=0.08)

    def test_sharpness_drops_after_blur(self):
        sharp, blurred = demo_images()
        for sharp_score, blurred_score in zip(focus_scores(sharp), focus_scores(blurred)):
            self.assertGreater(sharp_score, blurred_score)


if __name__ == "__main__":
    unittest.main()
