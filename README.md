# OmniGuard

OmniGuard is a Python-based utility designed to optimize memory usage in Windows, enhancing application performance and system stability. It periodically checks the system's memory usage and attempts to free up RAM if necessary.

## Features

- Monitors system memory usage.
- Frees up RAM when available memory falls below 20% of the total memory.
- Logs actions and system memory status to a log file.

## Requirements

- Windows operating system.
- Python 3.x.
- `psutil` library (install using `pip install psutil`).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/omniguard.git
    cd omniguard
    ```

2. Install the required Python package:

    ```bash
    pip install psutil
    ```

## Usage

Run the script using Python:

```bash
python omniguard.py
```

The program will start monitoring and optimizing memory usage every 60 seconds. Log entries will be saved in `omniguard.log`.

## Disclaimer

OmniGuard uses the Windows API to manage memory, which might have varying effects depending on system configuration and running applications. Use at your own risk and ensure regular backups of important data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.