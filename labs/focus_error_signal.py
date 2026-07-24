"""A simple astigmatic focus-error sweep using paraxial ray matrices."""
from __future__ import annotations

import numpy as np


def translation(distance_mm: float) -> np.ndarray:
    return np.array([[1.0, distance_mm], [0.0, 1.0]])


def lens(focal_length_mm: float) -> np.ndarray:
    return np.array([[1.0, 0.0], [-1.0 / focal_length_mm, 1.0]])


def mean_axis_difference(detector_mm: float, fx_mm: float = 100.0, fy_mm: float = 120.0) -> float:
    heights = np.linspace(-10.0, 10.0, 9)
    # A collimated input ray is first refracted, then propagated to the detector.
    system_x = translation(detector_mm) @ lens(fx_mm)
    system_y = translation(detector_mm) @ lens(fy_mm)
    differences = []
    for height in heights:
        ray = np.array([height, 0.0])
        differences.append(abs((system_x @ ray)[0] - (system_y @ ray)[0]))
    return float(np.mean(differences))


def detector_sweep() -> tuple[np.ndarray, np.ndarray]:
    distances = np.linspace(95.0, 125.0, 400)
    error = np.array([mean_axis_difference(distance) for distance in distances])
    return distances, error


if __name__ == "__main__":
    distances, error = detector_sweep()
    best = int(np.argmin(error))
    print(f"best illustrative detector distance: {distances[best]:.2f} mm")
