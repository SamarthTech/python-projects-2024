# QR Code Generator

This Python script generates a QR code for any URL or text provided by the user and saves it as an image file (`qrcode.jpg`). The script uses the `qrcode` library for QR code generation and allows basic customization for QR code size, error correction level, and colors.

## Features
- Accepts user input for URL or text to encode
- Generates QR codes with customizable size and error correction
- Saves the QR code as a `.jpg` image file
- Customizable fill and background colors

## Requirements

Ensure you have Python installed, along with the required dependencies. You can install them using `pip`:

```bash
pip install qrcode[pil]
```