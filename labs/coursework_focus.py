"""Reproduce the nine-ray model used in the astigmatic focus coursework."""

import numpy as np

INPUT_FOCAL_LENGTH_MM = 100.0
OUTPUT_PROPAGATION_MM = 300.0
RAY_HEIGHTS_MM = np.linspace(-10.0, 10.0, 9)


def translation(distance_mm):
    return np.array([[1.0, distance_mm], [0.0, 1.0]])


def lens(focal_length_mm):
    return np.array([[1.0, 0.0], [-1.0 / focal_length_mm, 1.0]])


def mean_axis_difference(distance_mm, offset_mm=0.0):
    """Compute the mean absolute detector-plane x/y ray-height difference."""
    ray_angles = np.full_like(RAY_HEIGHTS_MM, offset_mm / INPUT_FOCAL_LENGTH_MM)
    rays = np.vstack((RAY_HEIGHTS_MM, ray_angles))
    input_plane = translation(distance_mm) @ lens(INPUT_FOCAL_LENGTH_MM) @ rays
    output_x = translation(OUTPUT_PROPAGATION_MM) @ lens(100.0) @ input_plane
    output_y = translation(OUTPUT_PROPAGATION_MM) @ lens(120.0) @ input_plane
    return float(np.mean(np.abs(output_x[0] - output_y[0])))


def best_distance():
    candidates = np.linspace(95.0, 125.0, 400)
    errors = np.array([mean_axis_difference(distance) for distance in candidates])
    # The 400-point grid straddles the 100 mm optimum. Both middle points
    # have equal error to floating-point precision; use the reported upper sample.
    index = int(np.flatnonzero(np.isclose(errors, errors.min(), rtol=0.0, atol=1e-12))[-1])
    return float(candidates[index]), float(errors[index])


if __name__ == "__main__":
    distance, error = best_distance()
    print(f"Best coursework detector distance: {distance:.2f} mm (mean error {error:.5f} mm)")
    for offset in range(-30, 31, 10):
        print(f"Offset {offset:+3d} mm: FES {mean_axis_difference(distance, offset):.5f} mm")
