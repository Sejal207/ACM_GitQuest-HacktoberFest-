# QR Code Generator

## Introduction
This repository contains a Python-based QR code generator that allows users to create QR codes with their personal information. The application has a simple and intuitive interface built using Tkinter, with QR code generation handled by the `qrcode` library and image processing by `Pillow` (PIL). It supports saving QR codes to a user-specified location.

## Features
- **Easy-to-use interface**: Input personal details like phone number, name, age, and education.
- **QR code generation**: Creates QR codes based on the provided information.
- **Custom save location**: Users can choose where to save the generated QR codes.
- **Real-time preview**: Displays the generated QR code in the application.
- **Input validation**: Ensures all fields are filled in before generating the QR code.
- **Error handling**: Provides clear messages for issues like missing fields or invalid save locations.

## Requirements
- **Python 3.x**
- `Tkinter` (for the graphical interface)
- `qrcode` (for generating QR codes)
- `Pillow (PIL)` (for handling images)
- `resizeimage` (for resizing images)

## Installation and Usage

### Step 1: Fork the Repository
Fork this repository to your GitHub account by clicking the "Fork" button at the top of this page.

### Step 2: Clone the Forked Repository
After forking, clone the repository from **your account** to your local machine:
```bash
git clone https://github.com/<your-username>/ACM-GitQuest-HacktoberFest-2024.git
cd ACM-GitQuest-HacktoberFest-2024
git checkout qr-generator-application
```

### Step 3: Install Dependencies
Navigate to the project directory and install the required dependencies using the following command:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
To start the application, run:
```bash
python QR_Generator.py
```

### Step 5: Using the Application
- Enter your **phone number**, **name**, **age**, and **education** into the respective fields.
- Use the **Browse** button to choose a directory for saving your QR code.
- Click **Generate** to create the QR code, which will display within the application.
- To clear the fields and reset the form, click the **Clear** button.

## Building Executable
If you want to package this app as an executable:
1. Run the `setup.py` script to build a standalone executable using PyInstaller:
   ```bash
   python setup.py
   ```
   This will generate a standalone `.exe` file for easy distribution.

2. The generated executable can be found in the `dist` folder after the build process completes.

## Project Structure
```plaintext
├── .gitignore           # Ignored files/folders for version control
├── LICENSE              # MIT License
├── QR_Generator.py      # Main application script
├── README.md            # Project documentation
├── requirements.txt     # List of dependencies
├── setup.py             # Script to build executable and manage project setup
```

## License
This project is licensed under the MIT License. Feel free to use and modify the code as per the terms of the license.

---