# Verification and Validation Plan

## Purpose
Ensure that all software requirements are properly implemented and verified.

## Verification Activities
| Requirement | Method             | Evidence                          |
|-------------|--------------------|-----------------------------------|
| REQ-001     | Unit Test, Log     | test_timer.py, telemetry.log      |
| REQ-002     | Log Review         | telemetry.log output              |
| REQ-003     | Manual Test        | Console test and logs             |
| REQ-004     | Lint, Run Check    | flake8 output, platform support   |
| REQ-005     | Pytest             | pytest session output             |

## Validation
- Manual walkthrough of countdown
- Test coverage for known edge cases (0 seconds, negative input blocked, pause/resume)
- Log review to confirm proper sequencing
