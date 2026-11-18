# AOI and Computer-Vision Labs

[Portfolio case study](https://scandial-portfolio.scandium.chatgpt.site/project-aoi-coursework.html) · Run the coursework model to reproduce the portfolio's 100.04 mm sweep result and FES series. A separate two-lens exercise illustrates optical balance.

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

Install the Python dependencies with `python -m pip install -r requirements.txt`. Run `python -m labs.focus_error_signal` to sweep the detector plane. With focal lengths of 100 and 120 mm, the analytic balance of the two spot radii is approximately 109.09 mm. The sample grid reports the closest minimum. The public coursework implementation uses a different optical layout, including a 100 mm input lens and 300 mm output propagation. Run `python -m labs.coursework_focus` to reproduce the 100.04 mm result and FES values at axial offsets from −30 mm to +30 mm. The nearest samples on either side of the 100 mm optimum have equal error within numerical precision. The implementation selects the upper sample for consistency with the coursework report.

Run `python -m unittest discover -s tests -v` to check both optical models and the OpenCV sharpness comparison.

Run `python -m labs.sharpness` to compare Laplacian energy, Laplacian variance and Sobel energy before and after applying Gaussian blur to a generated image.

## License

Apache-2.0. See [LICENSE](LICENSE).
