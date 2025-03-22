# Anti-Keylogger Detection Tool

This Python script scans for potential keyloggers by detecting suspicious keyboard hooks and processes.

## Features
- Detects global keyboard hooks.
- Scans running processes for common keylogger names.
- Alerts users about potential threats.

## Installation
To install the required dependencies, run:
```sh
pip install psutil pywin32
```

## Usage
Run the script using:
```sh
python anti_keylogger.py
```
The script will scan for potential keyloggers and alert you if any suspicious activity is detected.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
"""
