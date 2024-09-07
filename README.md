# Auto Git Commit Script

This script automatically adds `.gitkeep` files to all empty folders (excluding the `.git` folder) in a specified directory, monitors the directory for changes, and commits them to a Git repository every 5 minutes (or a configurable interval). Additionally, it updates the script with a timestamp before each commit, ensuring the last commit time is recorded.

## Features

- Automatically adds `.gitkeep` files to empty directories.
- Monitors a specified folder for changes and commits them.
- Includes a timestamp in the `auto_git_commit.py` file to mark the last commit time.
- Configurable directory and commit check interval (default: 5 minutes).
- Runs as a background service on both Windows and Debian.

## Requirements

- Python 3.x
- Git installed and configured in your system
- `pyinstaller` (for building executables)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/auto-git-commit.git
   cd auto-git-commit
   ```

2. **Install Required Python Libraries:**

   Install `pyinstaller` if you want to compile the script into an executable:

   ```bash
   pip install pyinstaller
   ```

3. **Usage:**

   You can directly run the Python script or build it as an executable for both Windows and Debian.

### Running the Script Directly

```bash
python auto_git_commit.py --dir /path/to/your/directory --timer 300
```

- `--dir`: The directory you want to monitor for changes.
- `--timer`: Time in seconds between each check for changes (e.g., 300 seconds = 5 minutes).

### Building the Executable

#### For Windows:

1. Run the following command to build the executable:

   ```bash
   pyinstaller --onefile --noconsole auto_git_commit.py
   ```

2. Place the generated `auto_git_commit.exe` in the desired location.

3. Add the `.exe` to startup:

   - Press `Win + R`, type `shell:startup`, and press Enter.
   - Place a batch file in the startup folder that runs the executable, for example:

     ```batch
     @echo off
     start "" "C:\path\to\auto_git_commit.exe" --dir "C:\path\to\your\directory" --timer 300
     ```

#### For Debian

1. Build the executable:

   ```bash
   pyinstaller --onefile --noconsole auto_git_commit.py
   ```

2. Move the generated `auto_git_commit` binary to a location like `/usr/local/bin/`.

3. Create a `systemd` service to run it on startup:

   ```bash
   sudo nano /etc/systemd/system/auto_git_commit.service
   ```

   Add the following content:

   ```ini
   [Unit]
   Description=Auto Git Commit Service
   After=network.target

   [Service]
   ExecStart=/usr/local/bin/auto_git_commit --dir /path/to/your/directory --timer 300
   WorkingDirectory=/path/to/your/directory
   Restart=always
   User={ENTER YOUR USER}

   [Install]
   WantedBy=multi-user.target
   ```

4. Enable and start the service:

   ```bash
   sudo systemctl enable auto_git_commit.service
   sudo systemctl start auto_git_commit.service
   ```

## How It Works

1. **Add .gitkeep Files**:
   - The script traverses the specified directory and adds `.gitkeep` files to any empty subdirectories.

2. **Monitor and Commit Changes**:
   - Every 5 minutes (or the interval you specify), the script checks for changes in the directory.
   - If changes are detected, it:
     1. Appends the current timestamp to the `auto_git_commit.py` file.
     2. Adds and commits the changes to Git, including a timestamp in the commit message.

3. **Run on Startup**:
   - The script can be configured to run on startup both on Windows and Debian using either a batch file or a `systemd` service.

## License

This project is licensed under the [MIT License](LICENSE).
