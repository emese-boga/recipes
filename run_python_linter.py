#!/usr/bin/env python3
import subprocess


"""Run this script to format the files you changed"""


def main():
    modified_files = subprocess.check_output(
        "git ls-files -o -m --exclude-standard -- '*.py' | "
        "grep -vE ^$(git ls-files -d | paste -sd '|' -)$",
        shell=True,
        text=True,
    )
    if not modified_files:
        print("Nothing to check...")
        exit(0)

    has_failed = False

    print("Black output:")
    for file in modified_files.split():
        try:
            subprocess.run(["black", file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running black on {file}: {e}")
            has_failed = True

    print("Ruff output:")
    for file in modified_files.split():
        try:
            subprocess.run(["ruff", "check", file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running black on {file}: {e}")
            has_failed = True

    exit(int(has_failed))


if __name__ == "__main__":
    main()
