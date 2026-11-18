# AOI and Computer-Vision Labs

[Portfolio case study](https://scandial-portfolio.scandium.chatgpt.site/project-aoi-coursework.html) · The detector sweep in this repository is an illustrative two-lens exercise. The accompanying portfolio documents the separate coursework model.

Public, self-contained lab exercises inspired by coursework in geometrical optics, focusing, and image-based inspection. The repository contains clean educational implementations only: no course handouts, grading materials, student identifiers, or submitted reports.

## Labs

- Thin-lens image-distance sweep
- Parabolic-mirror ray geometry
- Astigmatic detector-distance sweep for a simple focus-error signal

## Setup

```powershell
python -m pip install -r requirements.txt
python labs/focus_error_signal.py
```

The scripts use Matplotlib's default plotting behavior and are intended for local exploration.

## Scope

These are educational simulations, not calibrated optical-design tools or inspection-machine software. Parameters are illustrative and should be replaced by measured values for any real AOI system.

## Reproduce the examples

Install the Python dependencies with `python -m pip install -r requirements.txt`. Run `python -m labs.focus_error_signal` to sweep the detector plane. With focal lengths of 100 and 120 mm, the analytic balance of the two spot radii is approximately 109.09 mm. The sample grid reports the closest minimum. The 100.04 mm result in the portfolio uses the separate coursework optical system.

Run `python -m labs.sharpness` to compare Laplacian energy, Laplacian variance and Sobel energy before and after applying Gaussian blur to a generated image.

## License

Apache-2.0. See [LICENSE](LICENSE).
