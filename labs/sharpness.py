"""Compare focus metrics on a reproducible synthetic image."""

import cv2
import numpy as np


def focus_scores(image: np.ndarray) -> tuple[float, float, float]:
    """Return Laplacian energy, Laplacian variance and mean Sobel energy."""
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    return (
        float(np.mean(laplacian ** 2)),
        float(np.var(laplacian)),
        float(np.mean(sobel_x ** 2 + sobel_y ** 2)),
    )


def demo_images() -> tuple[np.ndarray, np.ndarray]:
    sharp = np.zeros((128, 128), dtype=np.uint8)
    cv2.rectangle(sharp, (24, 24), (104, 104), 255, 2)
    blurred = cv2.GaussianBlur(sharp, (11, 11), 2.0)
    return sharp, blurred


if __name__ == "__main__":
    for name, frame in zip(("sharp", "blurred"), demo_images()):
        energy, variance, sobel = focus_scores(frame)
        print(f"{name}: Laplacian energy={energy:.2f}, variance={variance:.2f}, Sobel energy={sobel:.2f}")
