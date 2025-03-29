"""
Nejaky pokec o tom co dany skript dela
"""
import os
import time
import shutil
from datetime import datetime


def remove_old_logs_recursive(logs_path, days_old=28, print_to_console=True):
    now = time.time()
    cutoff = now - (days_old * 86400)

    log_filename = os.path.join(logs_path, "log_cleanup.txt")
    log_file = open(log_filename, "w", encoding="utf-8")

    def log(message):
        if print_to_console:
            print(message)
        log_file.write(message + "\n")

    log(f"{datetime.now()} - Start cleanup in {logs_path}")
    log(f"Deleting files and subdirectories older then {days_old} days.")
    log("-" * 60)

    for root, dirs, files in os.walk(logs_path, topdown=False):
        # removing .xml log files
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith('.xml'):
                try:
                    if os.path.getmtime(file_path) < cutoff:
                        os.remove(file_path)
                        print(f"Log file is deleted: {file_path}")
                        log(f"Log file is deleted: {file_path}")
                except OSError:
                    print(f"Skip unremovable file: {file_path}")
                    log(f"Skip unremovable file: {file_path}")

        # removing old subdirectories
        for subdir in dirs:
            subdir_path = os.path.join(root, subdir)
            try:
                if os.path.getmtime(subdir_path) < cutoff:
                    shutil.rmtree(subdir_path)
                    print(f"Subdirectory is deleted: {subdir_path}")
                    log(f"Subdirectory is deleted: {subdir_path}")
            except OSError:
                print(f"Skip unremovable subdirectory: {subdir_path}")
                log(f"Skip unremovable subdirectory: {subdir_path}")

    log("-" * 60)
    log("Cleanup is done.")
    full_log_path = os.path.abspath(log_filename)
    log(f"Log file of cleanup is saved: {full_log_path}")
    log_file.close()


logs_path = "cesta k adresari"
remove_old_logs_recursive(logs_path)
