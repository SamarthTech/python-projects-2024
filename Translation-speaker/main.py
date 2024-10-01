import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

# Function to recognize speech and convert to text
def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)  # Listen for input

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio)  # Convert speech to text using Google's recognizer
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from the speech recognition service.")

# Function to translate the recognized speech to the target language
def translate_text(text, target_language='es'):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    print(f"Translated Text ({target_language}): {translated.text}")
    return translated.text

# Function to convert the translated text to speech
def text_to_speech(text, language='es'):
    tts = gTTS(text=text, lang=language)  # Convert text to speech
    tts.save("translated_audio.mp3")  # Save the audio file
    print("Playing audio...")
    playsound("translated_audio.mp3")  # Play the audio file

# Function to ask the user for the target language
def choose_language():
    print("\nChoose a language for translation:")
    print("Example language codes: 'es' for Spanish,\n 'fr' for French,\n 'de' for German,\n 'hi' for Hindi,\n 'zh-cn' for Chinese,\n 'en' for English")
    language_code = input("Enter the language code you want to translate to: ")
    return language_code

# Main function that integrates everything
if __name__ == "__main__":
    # Step 1: Recognize Speech
    recognized_text = recognize_speech()

    if recognized_text:
        # Step 2: Ask the user for the target language
        target_language = choose_language()

        # Step 3: Translate Text to the chosen target language
        translated_text = translate_text(recognized_text, target_language)

        # Step 4: Convert Translated Text to Speech
        text_to_speech(translated_text, target_language)
