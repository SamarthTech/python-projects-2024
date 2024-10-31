# 📊 Emotion Pulse: Sentiment Analysis Tool

Dive into the emotional landscape of any text with Emotion Pulse! This powerful sentiment analysis tool uses Natural Language Processing (NLP) techniques to uncover the emotions and sentiments hidden within your text.

## 🌟 Features

- **Text Preprocessing**: Cleans and prepares your text for analysis
- **Emotion Detection**: Identifies emotions based on a custom emotion dictionary
- **Sentiment Analysis**: Utilizes VADER (Valence Aware Dictionary and sEntiment Reasoner) for sentiment scoring
- **Data Visualization**: Generates eye-catching graphs of emotional distribution
- **NLTK Integration**: Leverages the power of the Natural Language Toolkit for advanced NLP tasks

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/KoustavDeveloper/emotion-pulse.git
   cd emotion-pulse
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Download NLTK resources:
   ```python
   python settings.py
   ```

## 💻 Usage

1. Place your text file in the project directory as `read.txt`.

2. Run the analysis:
   ```
   python main_nltk.py
   ```

3. View the results in the console and check out the generated `graph.png` for a visual representation of emotions.

## 📊 Sample Output

```
Emotion Count: Counter({'happy': 5, 'angry': 3, 'sad': 2, 'surprise': 1})
Sentiment Score: {'neg': 0.092, 'neu': 0.808, 'pos': 0.1, 'compound': 0.0258}
Positive Sentiment
```

![Sample Emotion Graph](graph.png)

## 🛠 Customization

- Modify `emotions.txt` to add or change emotion categories
- Adjust stop words in `main_nltk.py` to fine-tune text processing

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/emotion-pulse/issues).

## 👏 Acknowledgements

- [NLTK](https://www.nltk.org/) for providing excellent NLP tools
- [VADER Sentiment](https://github.com/cjhutto/vaderSentiment) for sentiment analysis

---

Made with ❤️ and 🐍 by [Koustav Singh](https://github.com/KoustavDeveloper/)