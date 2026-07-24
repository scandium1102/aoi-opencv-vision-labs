"""Explore image distance with the thin-lens equation."""
from __future__ import annotations

import numpy as np


def image_distance(object_distance_mm: float, focal_length_mm: float) -> float:
    if object_distance_mm == focal_length_mm:
        raise ValueError("object distance cannot equal focal length")
    return 1.0 / (1.0 / focal_length_mm - 1.0 / object_distance_mm)


def sweep(focal_length_mm: float = 50.0) -> tuple[np.ndarray, np.ndarray]:
    objects = np.linspace(60.0, 500.0, 80)
    images = np.array([image_distance(distance, focal_length_mm) for distance in objects])
    return objects, images


if __name__ == "__main__":
    distances, images = sweep()
    print(f"image distance at {distances[0]:.1f} mm object distance: {images[0]:.2f} mm")
