# Duplicate File Remover
## Overview

This Python script identifies and removes duplicate files in a specified directory by comparing the hash values (MD5) of each file. It is designed to handle large files efficiently by reading them in blocks. The tool can be useful for cleaning up disk space by eliminating redundant copies of files.

## Features

- **Efficient File Hashing**: Uses the MD5 hashing algorithm to generate unique signatures for files.
- **Memory Efficient**: Handles large files by reading them in chunks instead of loading the entire file into memory at once.
- **Automatic Deletion**: Identifies and automatically deletes duplicate files.
- **Logs Deleted Files**: Keeps a record of all deleted files for reference.

## How It Works

1. The script computes an MD5 hash for each file in the directory.
2. It stores the hash in a dictionary (`hashMap`), with the hash as the key and the filename as the value.
3. If a file with the same hash (i.e., a duplicate) is found, the duplicate file is deleted, and its name is added to the `deletedFiles` list.
4. After processing all files, the script prints a list of all the deleted duplicate files.

## Usage

1. Place the script (`main.py`) in the directory where you want to scan for duplicate files.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:

```bash
python main.py
```

The script will automatically scan the current directory for duplicate files and delete them.

## Customization

- **Block Size**: The block size used to read large files is set to `65536` bytes by default. You can adjust this value in the `hashFile` function to suit your system's memory capacity.
- **Directory**: By default, the script operates in the current directory. You can modify it to take a specific directory as input if needed.

## Requirements

This script uses Python's built-in libraries:
- `os`: For file operations.
- `hashlib`: For generating MD5 hashes of files.

## Limitations

- The script uses MD5 hashing, which is fast but not cryptographically secure. For most duplicate detection tasks, this should suffice, but if more security is needed, consider switching to a stronger hash algorithm such as SHA-256.
- It operates only within the current directory. If you want to scan subdirectories as well, you will need to modify the file traversal logic.

---
