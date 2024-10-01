
# 🎙️ Speech-to-Speech Language Translator 🌐

This Python project enables real-time speech recognition, translation into multiple languages, and text-to-speech synthesis. With this tool, you can speak in one language, have it translated, and hear the translation in your target language all through a streamlined, user-friendly process.


## 🚀 Features

- Speech Recognition: Converts spoken words into text using Google's Speech Recognition API.
- Real-Time Translation: Automatically translates the recognized speech into your selected language using Google Translate.
- Text-to-Speech: Converts the translated text back into speech with Google Text-to-Speech (gTTS).
- Multi-Language Support: Translate your speech into any language supported by Google Translate, including:
  - es (Spanish)
  - fr (French)
  - de (German)
  - hi (Hindi)
  - zh-cn (Chinese)
  - and many more!


## 🛠️ Installation

Before running the project, make sure you have the following dependencies installed:

```bash
  pip install SpeechRecognition googletrans==4.0.0-rc1 gTTS playsound
```

Make sure to have ffmpeg installed as well, which is required to play the audio:

```bash
    # On MacOS:
    brew install ffmpeg

    # On Ubuntu:
    sudo apt install ffmpeg

    # On Windows:
    # Download the executable from https://ffmpeg.org/download.html and add it to your PATH.
```

## 📋 Usage
1. Clone the repository:

```javascript
git clone https://github.com/5haiqin/speech-translator.git
cd speech-translator
```
2. Run the script:

```javascript
python translator.py
```
3. Follow the instructions:
- Speak into your microphone when prompted.
- Choose the target language for translation using the language code.
- The recognized speech will be translated and played back in the selected language.

## 🧠 How It Works

- Speech Recognition: The recognize_speech() function listens to the user's voice input and converts it into text using Google's speech recognition engine.

- Translation: The translate_text() function uses Google Translate to translate the recognized text into the desired language.

- Text-to-Speech: The text_to_speech() function converts the translated text back into speech using Google Text-to-Speech (gTTS) and plays it using the playsound library.

## 🌍 Supported Languages

You can translate speech to any language supported by Google Translate. A few examples:

- es: Spanish
- fr: French
- de: German
- hi: Hindi
- zh-cn: Simplified Chinese
- en: English


Refer to Google Translate Language Codes for the full list.
## 📦 Project Structure

├── translator.py          # Main Python script

├── README.md              # Project documentation

└── requirements.txt       # List of dependencies



## 📝 License

This project is licensed under the MIT License. See the [LICENSE](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) file for details.

## 🤝 Contributions
Contributions, issues, and feature requests are welcome! Feel free to check out the [issues page](https://github.com/5haiqin/speech-translator/issues).




## 🌟 Acknowledgements

 - [Google Speech Recognition API](https://cloud.google.com/speech-to-text/docs/)
 - [Google Translate API](https://github.com/matiassingers/awesome-readme)
 - [Google Text-to-Speech (gTTS)](https://pypi.org/project/gTTS/)
 - [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/)
 - [Playsound](https://pypi.org/project/playsound/)


## 🎯 Future Improvements

- Add support for more advanced translation engines.
- Implement GUI for a better user experience.
- Enable saving translated speech files for offline access.


 Happy Coding! ✨