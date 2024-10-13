import subprocess
import sys
import os
import shutil


# Function to install PyInstaller if it's not already installed
def install_pyinstaller():
    try:
        # Attempt to install PyInstaller
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller==6.10.0"])
        print("PyInstaller installed successfully.")
    except subprocess.CalledProcessError as e:
        # Check if the error is due to PyInstaller already being installed
        if "already satisfied" in str(e):
            print("PyInstaller is already installed.")
        else:
            print(f"Error occurred while installing PyInstaller: {e}")
            sys.exit(1)


# Function to update .gitignore to exclude .exe files
def update_gitignore():
    gitignore_path = os.path.join(os.getcwd(), ".gitignore")
    exe_entry = "*.exe"

    # Check if .gitignore exists
    if os.path.exists(gitignore_path):
        # Read existing entries to check if the .exe entry already exists
        with open(gitignore_path, "r") as f:
            if exe_entry in f.read():
                print(f"'{exe_entry}' is already in .gitignore.")
                return
    else:
        print(".gitignore file does not exist. It will be created.")

    # Append the .exe entry to .gitignore
    with open(gitignore_path, "a") as f:
        f.write(f"{exe_entry}\n")
        print(f"Added '{exe_entry}' to .gitignore.")


# Function to activate virtual environment and run the PyInstaller command
def activate_venv_and_build():
    # Detect the correct activation script based on the operating system
    venv_dir = os.path.join(os.getcwd(), "venv", "Scripts" if os.name == "nt" else "bin")
    activate_script = os.path.join(venv_dir, "activate")

    # Activate the virtual environment
    if os.name == "nt":  # Windows
        activate_command = f"{activate_script} &&"
    else:  # macOS/Linux
        activate_command = f"source {activate_script} &&"

    try:
        # Run PyInstaller inside the activated virtual environment
        subprocess.check_call(
            f"{activate_command} pyinstaller --onefile --noconsole --exclude-module unittest --exclude-module email QR_Generator.py",
            shell=True)
        print("\033[92mExecutable built successfully.\033[0m")  # Print in green

        cleanup()

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while building the executable: {e}")
        sys.exit(1)


# Function to clean up unnecessary files and folders
def cleanup():
    # Move the contents of the dist folder to the parent directory of dist
    dist_folder = os.path.join(os.getcwd(), "dist")
    if os.path.exists(dist_folder):
        # Move all contents of the dist folder to its parent directory
        for item in os.listdir(dist_folder):
            shutil.move(os.path.join(dist_folder, item), os.path.join(os.getcwd(), item))

        # Remove the dist folder after moving the contents
        os.rmdir(dist_folder)

    # Remove the build folder if it exists
    build_folder = os.path.join(os.getcwd(), "build")
    if os.path.exists(build_folder):
        shutil.rmtree(build_folder)

    # Remove the .spec file if it exists
    spec_file = os.path.join(os.getcwd(), "QR_Generator.spec")
    if os.path.exists(spec_file):
        os.remove(spec_file)


if __name__ == "__main__":
    install_pyinstaller()  # Install PyInstaller before building
    update_gitignore()     # Update .gitignore to ignore .exe files
    activate_venv_and_build()  # Activate venv and build the executable
