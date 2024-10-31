# Morse Code Dictionary
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.',  'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': ' ', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '!': '-.-.--', '@': '.--.-.', '&': '.-...'
}

# Reverse dictionary for decoding
REVERSE_MORSE = {value: key for key, value in MORSE_CODE.items()}

def text_to_morse(text):
    """Convert text to Morse code."""
    try:
        morse = ' '.join(MORSE_CODE.get(char.upper(), '?') for char in text)
        return morse if morse else "Error: Empty input"
    except Exception as e:
        return f"Error converting text to Morse: {str(e)}"

def morse_to_text(morse):
    """Convert Morse code to text."""
    try:
        # Split morse code into individual signals
        words = morse.strip().split('   ')
        decoded_words = []
        
        for word in words:
            chars = word.split(' ')
            decoded_chars = [REVERSE_MORSE.get(char, '?') for char in chars if char]
            decoded_words.append(''.join(decoded_chars))
        
        return ' '.join(decoded_words)
    except Exception as e:
        return f"Error converting Morse to text: {str(e)}"

def play_morse_code(morse):
    """Play Morse code as sound (if playsound is installed)."""
    try:
        from playsound import playsound
        import numpy as np
        from scipy.io.wavfile import write
        import os

        # Define sound parameters
        SAMPLE_RATE = 44100
        FREQUENCY = 800
        DOT_DURATION = 0.1
        DASH_DURATION = DOT_DURATION * 3

        def generate_beep(duration):
            t = np.linspace(0, duration, int(SAMPLE_RATE * duration))
            return np.sin(2 * np.pi * FREQUENCY * t)

        # Generate audio data
        audio = []
        for symbol in morse:
            if symbol == '.':
                audio.extend(generate_beep(DOT_DURATION))
            elif symbol == '-':
                audio.extend(generate_beep(DASH_DURATION))
            elif symbol == ' ':
                audio.extend(np.zeros(int(SAMPLE_RATE * DOT_DURATION)))
            
            # Add small pause between symbols
            audio.extend(np.zeros(int(SAMPLE_RATE * 0.05)))

        # Normalize and convert to 16-bit integer
        audio = np.array(audio)
        audio = audio * 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)

        # Save and play
        write('morse.wav', SAMPLE_RATE, audio)
        playsound('morse.wav')
        os.remove('morse.wav')
        
    except ImportError:
        return "Please install playsound and scipy to enable sound playback: pip install playsound scipy"
    except Exception as e:
        return f"Error playing Morse code: {str(e)}"

def main():
    print("\n=== Morse Code Converter ===")
    print("1. Text to Morse")
    print("2. Morse to Text")
    print("3. Exit")
    
    while True:
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == '3':
            print("Goodbye!")
            break
            
        elif choice == '1':
            text = input("Enter text to convert: ")
            morse = text_to_morse(text)
            print(f"\nMorse Code: {morse}")
            
            if input("\nWould you like to hear it? (y/n): ").lower() == 'y':
                play_morse_code(morse.replace(' ', ''))
                
        elif choice == '2':
            print("\nFor Morse code input:")
            print("- Use dots (.) and dashes (-)")
            print("- Separate letters with spaces")
            print("- Separate words with three spaces")
            morse = input("\nEnter Morse code: ")
            text = morse_to_text(morse)
            print(f"\nDecoded Text: {text}")
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()