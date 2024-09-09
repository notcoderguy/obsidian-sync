import os
import subprocess
import time
import argparse
from datetime import datetime

CREATE_NO_WINDOW = 0x08000000

def add_gitkeep_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        if '.git' in root:
            continue
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            gitkeep_path = os.path.join(dir_path, '.gitkeep')
            if not os.listdir(dir_path):
                with open(gitkeep_path, 'w') as gitkeep_file:
                    pass
                print(f"Added .gitkeep to {dir_path}")

def git_commit(base_dir):
    os.chdir(base_dir)

    # Check for changes
    result = subprocess.run(['git', 'status', '--porcelain'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, creationflags=CREATE_NO_WINDOW, shell=False)
    if result.stdout:  # If there's any output, there are changes

        # Update the script with the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(__file__, 'a') as f:
            f.write(f"\n# Last commit timestamp: {timestamp}\n")

        subprocess.run(['git', 'add', '.'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=CREATE_NO_WINDOW, shell=False)
        subprocess.run(['git', 'commit', '-m', f'Automated commit at {timestamp}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=CREATE_NO_WINDOW, shell=False)
        print("Changes committed")
    else:
        print("No changes to commit")

def git_push(base_dir):
    os.chdir(base_dir)
    subprocess.run(['git', 'push'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=CREATE_NO_WINDOW, shell=False)

def git_pull(base_dir):
    os.chdir(base_dir)
    subprocess.run(['git', 'pull'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=CREATE_NO_WINDOW, shell=False)

def main():
    parser = argparse.ArgumentParser(description="Auto Git Commit Script")
    parser.add_argument('--dir', required=True, help='Directory to monitor for git commits')
    parser.add_argument('--timer', type=int, required=True, help='Time in seconds between each commit check')

    args = parser.parse_args()

    base_dir = args.dir
    sleep_timer = args.timer


    while True:
        git_pull(base_dir)
        add_gitkeep_files(base_dir)
        git_commit(base_dir)
        git_push(base_dir)
        time.sleep(sleep_timer)

if __name__ == "__main__":
    main()
