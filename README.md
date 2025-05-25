# 🚀 NASA Mission Timer Demo

This is a small educational software project that simulates a mission countdown timer with telemetry logging. It's structured to demonstrate high-level software engineering principles inspired by [NASA's NPR 7150.2D](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=main) standard for software development.

> **Note:** This is a demo project meant for learning and exploration. It is not intended for actual flight use or critical systems.

---

## 🎯 Project Goals

- Practice disciplined software engineering using NPR 7150.2D as a guide
- Implement a simple, testable system (a countdown timer) in Python
- Demonstrate process artifacts: requirements, design, verification, configuration management
- Explore how code structure, documentation, and validation tie into NASA-style standards

---

## 🧩 Features

- ✅ Countdown timer (with configurable time)
- ⏸ Pause, resume, and reset support
- 🧾 Telemetry log (timestamped events)
- 🧪 Unit tests for logic and state
- 📋 Requirements and validation documentation
- 📘 NPR 7150.2D compliance matrix

---

## 🛠️ Running the Project

Make sure you're using Python 3.8 or later.

```bash
python src/countdown_timer.py
```
You'll be prompted to enter a countdown time in seconds and then can control the timer with:

```bash
[s=start, p=pause, r=resume, x=reset, q=quit]
```

## ✅ Running Tests

Tests are written with pytest. From the project root:

# Install pytest if you haven't already
pip install pytest

# Run tests with proper path
PYTHONPATH=src pytest

## 📂 Project Structure

nasa-mission-timer-demo/
├── src/                         # Application code
│   └── countdown_timer.py
├── tests/                       # Unit tests
│   └── test_timer.py
├── docs/                        # Documentation per NPR 7150.2D
│   ├── software_requirements_specification.md
│   ├── software_design_description.md
│   ├── software_development_plan.md
│   ├── verification_validation_plan.md
│   └── npr_7150_2d_compliance_matrix.md
├── telemetry.log                # Output log of countdown events
├── README.md
└── .gitignore

## 🧠 Learn More

- 📄 [NPR 7150.2D - NASA Software Engineering Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_)
- 📝 [10 Rules for Developing Safety Critical Code (JPL)](https://plavos.com/blog/nasas-10-rules-for-space-proof-code/)
- 🧪 [pytest documentation](https://docs.pytest.org/en/stable/)

## 📜 License

This project is open source and available under the MIT License.