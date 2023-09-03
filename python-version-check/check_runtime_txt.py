import json
import os

def extract_python_version_from_pipfile_lock() -> str:
    """
    Extract the Python version specified in Pipfile.lock.
    
    Returns:
        str: Python version from Pipfile.lock.
    """
    with open("Pipfile.lock", "r", encoding='utf-8') as f:
        pipfile_lock_content = json.load(f)
    return pipfile_lock_content["_meta"]["requires"]["python_version"]

def extract_python_version_from_runtime_txt() -> str:
    """
    Extract the Python version specified in runtime.txt.
    
    Returns:
        str: Python version from runtime.txt.
    """
    with open("runtime.txt", "r", encoding='utf-8') as f:
        runtime_version = f.read().strip().split("-")[-1]
    return runtime_version

def main():
    """
    Main execution function. Compares the Python version from Pipfile.lock and runtime.txt.
    Exits with a non-zero status code if there's a mismatch or if files are missing.
    """
    if not os.path.exists("Pipfile.lock"):
        print("Error: Pipfile.lock does not exist!")
        exit(1)

    if not os.path.exists("runtime.txt"):
        print("Error: runtime.txt does not exist!")
        exit(1)

    pipfile_lock_version = extract_python_version_from_pipfile_lock()
    runtime_version = extract_python_version_from_runtime_txt()

    if pipfile_lock_version != runtime_version:
        print(f"Python version mismatch! Pipfile.lock: {pipfile_lock_version}, runtime.txt: {runtime_version}")
        exit(1)

if __name__ == "__main__":
    main()
