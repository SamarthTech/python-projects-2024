# Plagiarism Detector

## Overview

This project implements a plagiarism detector in Python. The detector compares a query text against a set of reference texts and identifies similarities using cosine similarity scores. It incorporates text preprocessing, feature extraction (Bag-of-Words and TF-IDF), and similarity calculation techniques.

## Files

1. **feature_extraction.py**: This file contains functions for extracting features from text using Bag-of-Words (BoW) and TF-IDF methods.

2. **preprocess.py**: The preprocessing module provides functions for text preprocessing, including tokenization, stop word removal, punctuation removal, and lemmatization.

3. **similarity_calculation.py**: Implements the calculation of similarity scores between query text and reference texts using cosine similarity.

4. **main.py**: The main script orchestrates the plagiarism detection process. It imports functions from other files to preprocess texts, extract features, calculate similarity scores, and identify plagiarized content.

## Dependencies

- **NLTK**: Natural Language Toolkit for text preprocessing.

```bash
pip3 install nltk
```
- **scikit-learn**: Library for machine learning tasks including feature extraction and similarity calculation.

Install dependencies using pip:

```bash
pip3 install nltk scikit-learn
```
Or

You can *install* **pip install -r requirements.txt** for the following dependencies


## Usage

1. Ensure all dependencies are installed.
2. Run the `main.py` script with your query text and reference texts. Modify the `query_text` and `reference_texts` variables in the script as needed.
3. To test for plagiarism using the provided example document and reference texts, follow these steps:

1. **Create Example Document**:
   - Create a text file named `example_document.txt` in the directory where your Python scripts are located.
   - Open the file with a text editor and paste the following content:
     ```
     Example Document

     This is an example document for testing plagiarism detection.
     It contains some text that may or may not be plagiarized from other sources.
     The goal is to identify any similarities between this document and the reference texts.
     ```

2. **Create Reference Texts**:
   - Create additional text files named `reference1.txt`, `reference2.txt`, etc., in the same directory.
   - Open each file with a text editor and paste the following content:

     `reference1.txt`:
     ```
     Reference Text 1

     This is the first reference text.
     It contains some unique content that may or may not be similar to the example document.
     ```

     `reference2.txt`:
     ```
     Reference Text 2

     This is the second reference text.
     It also contains some unique content for testing plagiarism detection.
     ```

3. **Modify `main.py`**:
   - Open `main.py` with a text editor and replace the existing code with the modified version provided earlier in this conversation.

4. **Run the Program**:
   - Open a terminal or command prompt.
   - Navigate to the directory where your Python scripts (`main.py`, `preprocess.py`, `feature_extraction.py`, `similarity_calculation.py`) and the text files (`example_document.txt`, `reference1.txt`, `reference2.txt`) are located.
   - Run the program using the command:
     ```
     python3 main.py
     ```

5. **Review Results**:
   - The program will execute and print the results indicating whether plagiarism was detected.
   - If plagiarism is detected, it will display the reference text(s) with similarity scores.
   - If no plagiarism is detected, it will print "No plagiarism detected."

Following these steps will allow you to test the plagiarism detection program using the provided example document and reference texts. Adjust the content of the files as needed for your testing purposes. The script will output detected plagiarized content along with their similarity scores, if any.




## Customization

- Adjust the threshold for similarity score in the `detect_plagiarism` function to control the sensitivity of plagiarism detection.
- Modify preprocessing techniques or feature extraction methods according to your requirements.
- Extend functionality by incorporating advanced similarity measures or additional features.

## Contributors

Feel free to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
