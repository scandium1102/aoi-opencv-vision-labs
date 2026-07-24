"""Compute normal slopes for a y = ax^2 parabolic mirror."""
from __future__ import annotations

import numpy as np


def mirror_profile(a: float = 0.02, width_mm: float = 20.0) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    x = np.linspace(-width_mm, width_mm, 101)
    y = a * x**2
    normal_slope = np.divide(-1.0, 2.0 * a * x, out=np.full_like(x, np.nan), where=x != 0)
    return x, y, normal_slope


if __name__ == "__main__":
    x, y, _ = mirror_profile()
    print(f"mirror samples: {len(x)}, vertex height: {y[len(y)//2]:.2f} mm")
