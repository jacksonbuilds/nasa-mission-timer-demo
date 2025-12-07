![Tests](https://github.com/jacksonbuilds/nasa-mission-timer-demo/actions/workflows/test.yml/badge.svg)
[![codecov](https://codecov.io/gh/jacksonbuilds/nasa-mission-timer-demo/branch/main/graph/badge.svg)](https://codecov.io/gh/jacksonbuilds/nasa-mission-timer-demo)

# NASA Mission Timer Demo

This is a small, educational Python package that simulates a mission countdown timer with telemetry logging. It's built to reflect software development principles inspired by [NASA's NPR 7150.2D](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_). The project includes a structured codebase, documentation, and tests to demonstrate good engineering discipline.

> **Note:** This is a demo project for learning purposes.

---

## Project Goals

- Build and package a modular countdown timer system
- Apply software engineering practices based on NPR 7150.2D
- Practice writing requirements, design docs, and test plans
- Implement a working telemetry logger with state control (pause/resume/reset)

---

## Installation

Clone the repo and install the package in editable mode:

```bash
git clone https://github.com/jacksonbuilds/nasa-mission-timer-demo.git
cd nasa-mission-timer-demo
pip install -e .
```
This allows you to edit the code and immediately see changes when running or testing

## Usage

You can run the timer from the command line:
```bash
python missiontimer/countdown_timer.py
```

## Testing

Use pytest for automated unit testing

To run tests:
```bash
pytest
```
If needed, install it:
```bash
pip install pytest
```
## Project Structure

```bash
nasa-mission-timer-demo/
├── missiontimer/                  # Python package
│   ├── __init__.py
│   └── countdown_timer.py
├── tests/                         # Unit tests
│   └── test_timer.py
├── docs/                          # Requirements, design, V&V, etc.
│   ├── software_requirements_specification.md
│   ├── software_design_description.md
│   ├── software_development_plan.md
│   ├── verification_validation_plan.md
│   └── npr_7150_2d_compliance_matrix.md
├── pyproject.toml
├── README.md
└── .gitignore
```

## Sample Telemetry Log

```bash
2025-05-25 12:00:01,123 T-minus 5 seconds
2025-05-25 12:00:02,124 T-minus 4 seconds
2025-05-25 12:00:03,127 T-minus 3 seconds
2025-05-25 12:00:04,128 T-minus 2 seconds
2025-05-25 12:00:05,129 T-minus 1 seconds
2025-05-25 12:00:06,130 Launch!
```

## Learn More

- [NPR 7150.2D - NASA Software Engineering Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_)
- [10 Rules for Developing Safety Critical Code (JPL)](https://plavos.com/blog/nasas-10-rules-for-space-proof-code/)
- [pytest documentation](https://docs.pytest.org/en/stable/)

## License

MIT License. See LICENSE file for details