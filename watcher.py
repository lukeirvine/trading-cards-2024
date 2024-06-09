import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Timer


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, script_to_run, ignore_folder):
        self.script_to_run = script_to_run
        self.timer = None
        self.debounce_delay = 1  # seconds
        self.ignore_folder = ignore_folder

    def on_any_event(self, event):
        # Ignore directories, temporary files, and files in the ignore folder
        if (
            event.is_directory
            or event.src_path.endswith(("~", ".swp", ".tmp"))
            or self.ignore_folder in event.src_path
        ):
            return
        print(f"{event.src_path} has been modified. Debouncing...")
        if self.timer:
            self.timer.cancel()
        self.timer = Timer(self.debounce_delay, self.run_script)
        self.timer.start()

    def run_script(self):
        print(f"Running {self.script_to_run}...")
        subprocess.call([sys.executable, self.script_to_run])


if __name__ == "__main__":
    path = "."  # The directory to watch
    script_to_run = "main.py"  # The script to run when a file changes
    ignore_folder = "output"  # Folder to ignore

    event_handler = ChangeHandler(script_to_run, ignore_folder)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print(f"Watching for changes in {path}, ignoring {ignore_folder}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
