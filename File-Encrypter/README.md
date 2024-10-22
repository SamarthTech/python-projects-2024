# File Encryption and Decryption Tool
## Overview

This Python script allows users to encrypt and decrypt files using the `cryptography` library, specifically with the `Fernet` encryption scheme. The script can generate a secret key to encrypt a file and later use the same key to decrypt it. This is a simple and efficient way to secure sensitive files by transforming them into an unreadable format unless the decryption key is provided.

## Features

- **File Encryption**: Encrypts any given file and saves the encrypted file with a `.encrypted` extension.
- **File Decryption**: Decrypts any previously encrypted file using the stored key and restores it to its original form.
- **Key Management**: Generates and saves a key for encryption, and loads the key for decryption from a file.

## Usage

The tool is designed to be run from the command line with the following syntax:

```bash
python main.py <file_path> <mode>
```

- `<file_path>`: Path to the file you want to encrypt or decrypt.
- `<mode>`: Operation mode: either `encrypt` to encrypt the file, or `decrypt` to decrypt the file.

### Example Commands

#### Encrypt a File
To encrypt a file, use the following command:

```bash
python main.py <file_name> encrypt
```

For example:

```bash
python main.py secret.txt encrypt
```

After running this, the file `secret.txt` will be encrypted, and a new file named `secret.encrypted` will be created. The original file (`secret.txt`) will be removed from the system. The key used for encryption will be saved as `secret.key`.

#### Decrypt a File
To decrypt a file, use the following command:

```bash
python main.py <file_name> decrypt
```

For example:

```bash
python main.py secret.encrypted decrypt
```

This will restore the original `secret.txt` file from the encrypted version. The encrypted file (`secret.encrypted`) will be removed after successful decryption.

### Key File
- The encryption key will be stored in a file named `secret.key`.
- Make sure to securely store this key, as it is essential for decryption. Losing the key will make the decryption of the file impossible.

## Code Explanation

### Functions

- **`generate_key()`**: Generates a key using the `Fernet.generate_key()` method.
- **`save_key(key, file_path)`**: Saves the generated key to a file (`secret.key`) in binary format.
- **`load_key(file_path)`**: Loads the key from the specified file (`secret.key`).
- **`encrypt_file(key, file_path)`**: Encrypts the specified file using the key, creates a new file with a `.encrypted` extension, and deletes the original file.
- **`decrypt_file(key, file_path)`**: Decrypts the specified `.encrypted` file using the key, recreates the original file with the `.txt` extension, and deletes the encrypted file.

### Command-Line Argument Parsing
- The script accepts two command-line arguments:
  1. The `file_path` of the file to be encrypted or decrypted.
  2. The `mode`, either `encrypt` or `decrypt`, to determine which operation to perform.

### Key File (`secret.key`)
- A secret key is automatically generated and saved to a file (`secret.key`) during the encryption process.
- This key file is loaded during the decryption process to restore the encrypted file.

## Security Notes

- **Keep the key secure**: The security of your encrypted files depends on the `secret.key` file. If this key is lost or compromised, the encrypted files cannot be decrypted.
- **Delete the key file when no longer needed**: If the key is not needed after decryption, consider securely deleting it to maintain security.

## Example Workflow

1. You have a sensitive file called `secret.txt` that you want to encrypt.
2. Run the encryption command:

    ```bash
    python main.py secret.txt encrypt
    ```

    This will generate a key, encrypt the file into `secret.encrypted`, and remove the original `secret.txt`.

3. If you want to decrypt the file back to its original form, run the following command:

    ```bash
    python main.py secret.encrypted decrypt
    ```

    This will recreate the original `secret.txt` and remove the encrypted version.

## Limitations

- The script currently works only with single files. Batch processing multiple files at once would require additional modifications.
- The key is stored as a file (`secret.key`) and must be handled securely to avoid compromising the encryption.

---
