# AOI and Computer-Vision Labs

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

## License

Apache-2.0. See [LICENSE](LICENSE).
