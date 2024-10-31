# Morse Code Converter

A versatile Python application that converts text to Morse code and vice versa, with audio playback capabilities. This interactive tool supports a wide range of characters including letters, numbers, and special symbols.

## 🌟 Features

- **Bidirectional Conversion**
  - Text to Morse code translation
  - Morse code to text translation
  - Support for uppercase and lowercase letters
  - Numbers and special characters support

- **Audio Playback**
  - Listen to Morse code signals
  - Customizable sound frequency and duration
  - Proper timing between dots and dashes

- **User-Friendly Interface**
  - Interactive command-line menu
  - Clear instructions and prompts
  - Error handling and validation
  - Clean and formatted output

## 📋 Requirements

- Python 3.6 or higher
- Required packages:
  ```
  playsound
  scipy
  numpy
  ```


## 💻 Usage

Run the program:
```bash
python main.py
```

### Menu Options:
1. **Text to Morse**: Convert regular text to Morse code
   - Enter your text when prompted
   - View the Morse code output
   - Choose to play the audio version

2. **Morse to Text**: Convert Morse code back to regular text
   - Follow the input format guidelines:
     - Use dots (.) and dashes (-)
     - Separate letters with single spaces
     - Separate words with three spaces
   - View the decoded text output

3. **Exit**: Close the program

### Input Examples:

```
# Text to Morse
Enter text to convert: Hello World
Output: .... . .-.. .-.. ---   .-- --- .-. .-.. -..

# Morse to Text
Enter Morse code: .... . .-.. .-.. ---   .-- --- .-. .-.. -..
Output: HELLO WORLD
```

## 📝 Supported Characters

### Letters
- A-Z (case insensitive)
- Full international alphabet support

### Numbers
- 0-9

### Special Characters
- Space: Separates words (represented by 3 spaces in Morse)
- Comma: --..--
- Period: .-.-.-
- Question Mark: ..--..
- Exclamation Mark: -.-.--
- At Symbol (@): .--.-.
- Ampersand (&): .-...

## 🎵 Audio Playback

The audio playback feature uses the following timing:
- Dot: 0.1 seconds
- Dash: 0.3 seconds (3x dot duration)
- Inter-element gap: 0.05 seconds
- Letter gap: 0.1 seconds
- Word gap: 0.3 seconds

## 🛠️ Technical Details

### Code Structure
- `MORSE_CODE`: Dictionary containing character to Morse code mappings
- `REVERSE_MORSE`: Inverse dictionary for decoding
- `text_to_morse()`: Converts text to Morse code
- `morse_to_text()`: Converts Morse code to text
- `play_morse_code()`: Generates and plays audio
- `main()`: Handles the user interface and program flow

### Error Handling
- Invalid input protection
- Proper error messages
- Graceful exit options

---
