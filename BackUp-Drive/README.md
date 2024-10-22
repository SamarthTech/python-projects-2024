# Back-Up Drive

This Python script allows users to check mounted storage devices and perform backup operations between different storage devices. The user can interact with the script through a simple command-line interface, which includes options to view mounted devices and backup files from one drive to another.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Functions Overview](#functions-overview)
- [Error Handling](#error-handling)
- [Notes](#notes)

---

## Features
1. **Storage Device Mount Checker**: 
   - Check mounted storage devices like removable drives (USB), local disks, network drives, and CD-ROMs.
2. **Backup Functionality**: 
   - Copy data from one storage device to another (supports both files and directories).
3. **Interactive User Input**: 
   - User-friendly interface to choose between device checking or data backup.

---

## Prerequisites
To run this script, you need:
- **Python 3.x** installed.
- Windows operating system (the script uses `wmic`, which is specific to Windows for device queries).

### Python Packages:
This script uses the built-in Python libraries:
- `subprocess`
- `time`
- `os`
- `shutil`

No external packages are required.

---

## Usage

1. **Run the Script**:
   - Save the script in a `.py` file.
   - Open the command prompt or terminal and navigate to the script directory.
   - Run the script using: 
     ```bash
     python main.py
     ```

2. **Choose an Option**:
   The script will present a prompt with the following options:
   ```bash
   Backup Mounter 
   1. To View Mounted Devices 
   2. Backup 
   3. Exit 
   Choose the above options to proceed: 
   ```

3. **Check Mounted Devices**:
   - Select option `1` to view mounted devices.
   - The script will further prompt you to choose the type of device you want to check:
     - `1`: Pendrive and SD Card
     - `2`: Local Disk
     - `3`: Network Mount
     - `4`: CD-ROM

4. **Perform Backup**:
   - Select option `2` to perform a backup.
   - Input the **FROM** and **TO** drive IDs (e.g., `D:`, `E:`) when prompted.
   - The backup will copy files and directories from the source drive to the destination drive.

5. **Exit**:
   - Select option `3` to exit the script.

---

## Functions Overview

### `storage_mount_check(n)`
This function checks the mounted devices based on the type selected by the user. It utilizes `wmic` commands to list the storage devices of a particular type.

- **Parameters**:
  - `n`: integer (1 for removable drives, 2 for local disks, 3 for network drives, 4 for CD-ROMs).
  
- **Output**: Returns the list of mounted devices or "Invalid Input" for incorrect selections.

### `backup(src, dst, symlinks=False, ignore=None)`
This function copies files and directories from the source to the destination.

- **Parameters**:
  - `src`: Source path (drive or directory).
  - `dst`: Destination path.
  - `symlinks`: Boolean (whether to copy symlinks, defaults to `False`).
  - `ignore`: Function to ignore files during the copy (optional).
  
- **Output**: Copies files and directories from `src` to `dst`.

### `usr_ip()`
This is the main interactive function that handles user input, provides options to check mounted devices, and perform backups.

---

## Error Handling

- **Invalid Input**: 
  If the user enters an invalid choice for viewing devices, the script will return `'Invalid Input'`.
  
- **Exceptions**: 
  This script does not include detailed error handling for exceptions like file I/O errors (e.g., permission issues, non-existent directories). These can be added based on the specific use case.

---

## Notes
- **OS Dependency**: This script is designed for **Windows**. If you're using a different operating system, the `wmic` commands will not work, and you will need to adapt the script for that OS.
  
- **Backup Speed**: The speed of the backup operation will depend on the size of the files and the speed of the source and destination storage devices.

---
