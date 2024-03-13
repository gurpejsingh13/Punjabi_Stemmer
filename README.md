# PunjabiStemmer
## Introduction
The PunjabiStemmer introduces a groundbreaking advancement in Natural Language Processing (NLP) for Punjabi, a major regional language in India. It combines rule-based and dictionary-based methodologies to address the morphological complexity of Punjabi, setting a new benchmark in linguistic technology.

Featuring over 300 suffix rules and a comprehensive database of over 50,000 words, the stemmer excels in handling various grammatical scenarios while preserving semantic integrity. This hybrid approach allows for meticulous processing across nouns, pronouns, adjectives, adverbs, verbs, and more, maintaining the essence of words and supporting diverse NLP applications.

Now available on PyPI, PunjabiStemmer is a monumental leap in text processing for regional languages, inviting collaboration and innovation in the field.
This Punjabi Stemmer was developed by Gurpej Singh, a researcher and software engineer dedicated to advancing Natural Language Processing for Punjabi, as part of his research work. 
## Main Features

The Punjabi_Stemmer package offers several functionalities, including:
1. **Stemming single word for testing.**
2. **Stemming a Sentence or Paragraph.**
3. **Stemming Content from a Large Text File.**
4. **Hybrid approach( Rule-Based + Dictionary Based Approach):** Incorporates over 300 specific rules and a comprehensive database of over 50,000 words, to precisely manage the linguistic diversity of Punjabi, effectively dealing with suffixes, prefixes, and more.
5. **High Accuracy:** Designed to minimize overstemming and understemming errors, enhancing the reliability of subsequent NLP tasks.
6. **Open Source:** Fully open-source, encouraging contributions, improvements, and customization to meet diverse needs.


You can install Punjabi_Stemmer directly from PyPI

## Installation
Before installing Punjabi Stemmer, ensure you have Python 3.7 or newer installed on your system. Punjabi Stemmer also require some other libraries installation:
```python
pip install regex
pip install os-sys
pip install collection
```
Install `Punjabi_Stemmer` using pip:

```python
pip install punjabi_stemmer
```

# Usage
Here's how to use the Punjabi_Stemmer Package in your Python projects:

## Stemming a Single Word
To stem a single Punjabi word, use the stem_word method:
```python
from Punjabi_Stemmer.Stemmer import PunjabiStemmer

# Now you can simply initialize the stemmer without specifying file paths
stemmer = PunjabiStemmer()

word = "ਭੱਜਣਾ"  # Example Punjabi word
stemmed_word = stemmer.stem_word(word)
print(f"Original: {word}, Stemmed: {stemmed_word}")

```
Output
```
ਭੱਜ
```
This will print the original word and its stemmed version.

## Stemming a Sentence or Paragraph
To stem a longer piece of text, such as a sentence or paragraph, use the stem_text method:
```python
from Punjabi_Stemmer.Stemmer import PunjabiStemmer

# Now you can simply initialize the stemmer without specifying file paths
stemmer = PunjabiStemmer()

text = "ਪੜਾਉਂਦਾ ਪੜਾਉਂਦੀ ਪੜਾਉਂਦੇ  ਪੜਾਉਣੀਆਂ  ਪੜਾਉਣੀ  ਪੜਾਉਣੇ ਪੜਾਂਦਾ ਪੜਾਂਦੀ"
stemmed_text = stemmer.stem_text(text)
print(f"Original: {text}\nStemmed: {stemmed_text}")

```
Output
```
ਪੜਾ ਪੜਾ ਪੜਾ ਪੜਾ ਪੜਾ ਪੜਾ ਪੜਾ ਪੜਾ
```
This will output the original text and the stemmed version.


## Stemming Content from a Text File
To process text from a file, ensuring all the content is automatically preprocessed and stemmed, then outputted to another file, you can use the stem_file method:
```python
from Punjabi_Stemmer.Stemmer import PunjabiStemmer

# Now you can simply initialize the stemmer without specifying file paths
stemmer = PunjabiStemmer()

input_file_path = 'path/to/your/input.txt'  # Path to your input file
output_file_path = 'path/to/your/output.txt'  # Path where you want to save the output

# Stem the content of the input file and save it to the output file
stemmer.stem_file(input_file_path, output_file_path)

```
Output
```
Processed text has been saved to D:/output.txt
```
Make sure the input file exists at the specified path; otherwise, you'll receive an error message.

These steps provide a comprehensive guide on how to use the Punjabi Stemmer package from basic to more advanced use cases, including processing individual words, text, and files. This should cover most needs users might have when working with Punjabi text data.

## Punjabi Stemmer Algorithm
```python
Step 1: Initialization

Load lists of pronouns, adverbs, post-positions, vocabulary, names, and suffixes.
Load the dictionary, organized alphabetically.

Step 2: Input Processing

Split the input text into individual words.
For each word in the split text:

Step 3: List Category Checking

a. If the length of the word is 1, output the word and move to the next one.
b. If the word is found in any loaded list (pronouns, adverbs, postpositions, vocabulary, names, suffixes), output the word and move to the next one.

Step 4: Apply Suffix Rule

a. If a suffix rule matches, apply it to stem the word.
b. If no suffix rule matches, output the original word and continue.

Step 5: Single-Character Check

If the length of the stemmed word is 1, output the original word and continue.

Step 6: Dictionary Validation and Further Stemming

a. If the stemmed word is validated in the dictionary, output the stemmed word.
b. If the stemmed word is not validated but the original word is:
i. Apply further suffix rules iteratively to the original word.
ii. If a valid stemmed word is found during iteration, output it.
iii. If no valid stem is found after all iterations, output the original word.
c. If neither the stemmed word nor the original word is validated in the dictionary, output the stemmed word.

```

## Rules Overview
In the development of the PunjabiStemmer, one of our core objectives was to create a highly accurate and versatile tool capable of navigating the rich morphological landscape of the Punjabi language. To achieve this, we have meticulously developed and implemented an expansive set of rules that serve as the foundation of our stemming process.

The PunjabiStemmer incorporates over 300 specific rules, designed to accurately process a wide array of grammatical scenarios. These rules are meticulously categorized to address different aspects of the language, including but not limited to, proper nouns and names, pronouns, verbs, adverbs, and adjectives. This structured approach allows the stemmer to precisely identify and handle the morphological nuances of Punjabi, significantly reducing errors related to overstemming and understemming.

Our research paper details about 160 of these rules, showcasing their application across various linguistic categories. To ensure comprehensive understanding and transparency, we've included the entire rule set in stemmer file in this repossitory https://github.com/gurpejsingh13/Punjabi_Stemmer.git

The rules are thoughtfully crafted and arranged from longest to smallest, optimizing both accuracy and efficiency in stemming. This organization reflects our meticulous approach to handling the complexities of Punjabi morphology.

We encourage users and developers to explore this detailed compilation of rules. It highlights the PunjabiStemmer's effectiveness and our dedication to advancing the field of Punjabi language processing.


## Contributing
Contributions to punjabi_stopwords are welcome! If you have suggestions for additional rules, or improvements to the existing list, please feel free to contribute.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
