# PunjabiStemmer
## Introduction
The PunjabiStemmer introduces a groundbreaking advancement in Natural Language Processing (NLP) for Punjabi, a major regional language in India. With an accuracy of 92.5%, it combines rule-based and dictionary-based methodologies to address the morphological complexity of Punjabi, setting a new benchmark in linguistic technology.

Featuring over 300 suffix rules and a comprehensive database of over 50,000 words, the stemmer excels in handling various grammatical scenarios while preserving semantic integrity. This hybrid approach allows for meticulous processing across nouns, pronouns, adjectives, adverbs, verbs, and more, maintaining the essence of words and supporting diverse NLP applications.

Now available on PyPI, PunjabiStemmer is a monumental leap in text processing for regional languages, inviting collaboration and innovation in the field.
This Punjabi Stemmer was developed by Gurpej Singh, a researcher dedicated to advancing Natural Language Processing for Punjabi, as part of his research work. 
## Main Features

The Punjabi_Stemmer package offers several functionalities, including:
1. Identifying Punjabi stopwords in text.
2. Removing Punjabi stopwords from text.
3. Adding custom stopwords to the existing list.

## Install the Package

You can install Punjabi_Stemmer directly from PyPI

## Installation

Install `Punjabi_Stemmer` using pip:

```python
pip install Punjabi_stemmer
```
# Usage
Here's how to use the Punjabi_Stemmer Package in your Python projects:

## Check root word for single word

## Rules Overview
In the development of the PunjabiStemmer, one of our core objectives was to create a highly accurate and versatile tool capable of navigating the rich morphological landscape of the Punjabi language. To achieve this, we have meticulously developed and implemented an expansive set of rules that serve as the foundation of our stemming process.

The PunjabiStemmer incorporates over 300 specific rules, designed to accurately process a wide array of grammatical scenarios. These rules are meticulously categorized to address different aspects of the language, including but not limited to, proper nouns and names, pronouns, verbs, adverbs, and adjectives. This structured approach allows the stemmer to precisely identify and handle the morphological nuances of Punjabi, significantly reducing errors related to overstemming and understemming.

Our research paper details about 160 of these rules, showcasing their application across various linguistic categories. To ensure comprehensive understanding and transparency, we've included the entire rule set in this README. This allows for a deeper dive into the methodology behind our stemmer, which boasts a remarkable 92.5% accuracy rate.

The rules are thoughtfully crafted and arranged from longest to smallest, optimizing both accuracy and efficiency in stemming. This organization reflects our meticulous approach to handling the complexities of Punjabi morphology.

We encourage users and developers to explore this detailed compilation of rules. It highlights the PunjabiStemmer's effectiveness and our dedication to advancing the field of Punjabi language processing.

```python
{"match": "ਪ੍ਰਰਸਤੀ", "strip": "ਪ੍ਰਰਸਤੀ", "add": ""},
{"match": "ਪੂਰਵਕ", "strip": "ਪੂਰਵਕ", "add": ""},
{"match": "ਉਦਿਆਂ", "strip": "ਉਦਿਆਂ", "add": ""},
{"match": "ਉਂਦੀਆਂ", "strip": "ਉਂਦੀਆਂ", "add": ""},
{"match": "ਉਦੀਆਂ", "strip": "ਉਦੀਆਂ", "add": ""},
{"match": "ਉਣੀਆਂ", "strip": "ਉਣੀਆਂ", "add": ""},
{"match": "ਅਈਆ", "strip": "ਅਈਆ", "add": ""},
{"match": "ਅਤਣ",  "strip": "ਣ", "add": ""},
{"match": "ਆਵਣ", "strip": "ਵਣ", "add": ""},
{"match": "ਆਵਣੀ", "strip": "ਆਵਣੀ", "add": ""},
{"match": "ਊਗੜਾ", "strip": "ਊਗੜਾ", "add": ""},
{"match": "ਕਰਣ", "strip": "ਕਰਣ", "add": ""},
{"match": "ਕਾਰਕ", "strip": "ਕਾਰਕ", "add": ""},
{"match": "ਜਨਕ", "strip": "ਜਨਕ", "add": ""},
{"match": "ਗਰਦੀ", "strip": "ਗਰਦੀ", "add": ""},
{"match": "ਤੰਤਰ", "strip": "ਤੰਤਰ", "add": ""},
{"match": "ਦਾਇਕ", "strip": "ਦਾਇਕ", "add": " "},
{"match": "ਦਾਰਨੀ", "strip": "ਦਾਰਨੀ", "add": "ਦਾਰਨੀ"},
{"match": "ਨਵੀਸ", "strip": "ਨਵੀਸ", "add": " "},
{"match": "ਪ੍ਰਸਤ", "strip": "ਪ੍ਰਸਤ", "add": " "},
{"match": "ਪਾਤਰ", "strip": "ਪਾਤਰ", "add": " "},
{"match": "'ਪੂਰਣ", "strip": "'ਪੂਰਣ", "add": " "},
{"match": "ਸ਼ਕਤੀ", "strip": "ਸ਼ਕਤੀ", "add": " "},
{"match": "ਸ਼ੀਲਤਾ", "strip": "ਸ਼ੀਲਤਾ", "add": " "},
{"match": "ਵਾਂਗੀਆ", "strip": "ਵਾਂਗੀਆ", "add": ""},
{"match": "ਾਵਾਂਗਾ", "strip": "ਵਾਂਗਾ", "add": ""},
{"match": "ਾਵਾਂਗੀ", "strip": "ਵਾਂਗੀ", "add": ""},
{"match": "ਾਵਾਂਗੇ", "strip": "ਵਾਂਗੇ", "add": ""},
{"match": 'ੀਕਰਨ', "strip": 'ੀਕਰਨ', "add": " "},
{"match": " ੀਕਰਨ", "strip": " ੀਕਰਨ", "add": ""},
{"match": "ਉਂਦਾ", "strip": "ਉਂਦਾ", "add": ""},
{"match": "ਉਂਦੀ", "strip": "ਉਂਦੀ", "add": ""},
{"match": "ਉਂਦੇ", "strip": "ਉਂਦੇ", "add": ""},
{"match": "ਉਣਾ", "strip": "ਉਣਾ", "add": ""},
{"match": "ਉਣੀ", "strip": "ਉਣੀ", "add": ""},
{"match": "ਉਣੇ", "strip": "ਉਣੇ", "add": ""},
{"match": "ਓਣ", "strip": "ਓਣ", "add": ""},
{"match": "ਓਗੇ", "strip": "ਓਗੇ", "add": ""},
{"match": "ਅਈ", "strip": "ਅਈ", "add": ""},
{"match": "ਅਣ", "strip": "ਅਣ", "add": ""},
{"match": "ਅਤ", "strip": "ਅਤ", "add": ""},
{"match": "ਆਈ", "strip": "ਆਈ", "add": ""},
{"match": "ਆਉ", "strip": "ਆਉ", "add": ""},
{"match": "ਆਉਂ", "strip": "ਆਉਂ", "add": ""},
{"match": "ਆਕ", "strip": "ਆਕ", "add": ""},
{"match": "ਆਣੀ", "strip": "ਆਣੀ", "add": ""},
{"match": "ਆਨੀ", "strip": "ਆਨੀ", "add": ""},
{"match": "ਆਰ", "strip": "ਆਰ", "add": ""},
{"match": "ਆਰਾ", "strip": "ਆਰਾ", "add": ""},
{"match": "ਆਰੀ", "strip": "ਆਰੀ", "add": ""},
{"match": "ਆਲ", "strip": "ਆਲ", "add": ""},
{"match": "ਆਲਾ", "strip": "ਆਲਾ", "add": ""},
{"match": "ਆਲੂ", "strip": "ਆਲੂ", "add": ""},
{"match": "ਐਲ", "strip": "ਐਲ", "add": ""},
{"match": "ਆੜੀ", "strip": "ਆੜੀ", "add": ""},
{"match": "ਇਕ", "strip": "ਇਕ", "add": ""},
{"match": "ਇਤ", "strip": "ਇਤ", "add": ""},
{"match": "ਈਆਂ", "strip": "ਈਆਂ", "add": ""},
{"match": "ਇਆ", "strip": "ਇਆ", "add": ""},
{"match": "ਇਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ਇਆਂ", "strip": "ਇਆਂ", "add": ""},
{"match": "ਈਆ", "strip": "ਆ", "add": ""},
{"match": "ਈਆ", "strip": "ਈਆ", "add": ""},
{"match": "ੲੀਆ", "strip": "ਆ", "add": ""},
{"match": "ਈਨ", "strip": "ਈਨ", "add": ""},
{"match": "ਇਏ", "strip": "ਇਏ", "add": ""},
{"match": "ਈਏ", "strip": "ਈਏ", "add": ""},
{"match": "ਏਟਾ", "strip": "ਏਟਾ", "add": ""},
{"match": "ਏਟੀ", "strip": "ਏਟੀ", "add": ""},
{"match": "ਏਰਾ", "strip": "ਏਰਾ", "add": ""},
{"match": "ਏਲੀ", "strip": "ਏਲੀ", "add": ""},
{"match": "ਈਲਾ", "strip": "ਈਲਾ", "add": ""},
{"match": "ਏਗਾ", "strip": "ਏਗਾ", "add": ""},
{"match": "ਏਗੀ", "strip": "ਏਗੀ", "add": ""},
{"match": "ਕਾਰ", "strip": "ਕਾਰ", "add": ""},
{"match": "ਕਾਰੀ", "strip": "ਕਾਰੀ", "add": ""},
{"match": "ਕੁਸ਼ੀ", "strip": "ਕੁਸ਼ੀ", "add": ""},
{"match": "ਖੋਰਾਂ", "strip": "ਖੋਰਾਂ", "add": ""},
{"match": "ਖ਼ੋਰ", "strip": "ਖ਼ੋਰ", "add": ""},
{"match": "ਖੋਰ", "strip": "ਖੋਰ", "add": ""},
{"match": "ਖ਼ਾਨਾ", "strip": "ਖ਼ਾਨਾ", "add": ""},
{"match": "ਗਾਰ", "strip": "ਗਾਰ", "add": ""},
{"match": "ਗਿਰੀ", "strip": "ਗਿਰੀ", "add": ""},
{"match": "ਗੀਰ", "strip": "ਗੀਰ", "add": ""},
{"match": "ਗਰ", "strip": "ਗਰ", "add": "ਗਰ"},
{"match": "ਗ਼ਰ", "strip": "ਗ਼ਰ", "add": "ਗ਼ਰ"},
{"match": "ਘਰ", "strip": "ਘਰ", "add": ""},
{"match": "ਘਣੀ", "strip": "ਘਣੀ", "add": "ਘਣੀ"}, #ਸਿੰਘਣੀ
{"match": "ਘਾਤ", "strip": "ਘਾਤ", "add": ""},
{"match": "ਚਾਰੀ", "strip": "ਚਾਰੀ", "add": ""},
{"match": "ਤਣ", "strip": "ਣ", "add": ""},
{"match": "ਤਰ", "strip": "ਤਰ", "add": ""},
{"match": "ਤਾਈ", "strip": "ਤਾਈ", "add": ""},
{"match": "ਤੇਰਾ", "strip": "ਤੇਰਾ", "add": ""},
{"match": "ਦਾਨ", "strip": "ਦਾਨ", "add": ""},
{"match": "ਦਾਰੀ", "strip": "ਦਾਰੀ", "add": ""},
{"match": "ਦਿਲ", "strip": "ਦਿਲ", "add": ""},
{"match": "ਦੀਆਂ", "strip": "ਆਂ", "add": ""}, # ਕੈਦੀਆਂ
{"match": "ਦੀਆਂ", "strip": "ਦੀਆਂ", "add": ""},
{"match": "ਂਦੀਆ", "strip": "ਂਦੀਆ", "add": ""},
{"match": "ਦਿਆ", "strip": "ਦਿਆ", "add": ""},
{"match": "ਦੀਆ", "strip": "ਆ", "add": ""},
{"match": "ਧਰ", "strip": "ਧਰ", "add": ""},
{"match": "ਧਾਰ", "strip": "ਧਾਰ", "add": ""},
{"match": "ਧਾਰੀ", "strip": "ਧਾਰੀ", "add": ""},
{"match": "ਨਾਕ", "strip": "ਨਾਕ", "add": ""},
{"match": "ਨੀਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ਨੀਆਂ", "strip": "ੀਆਂ", "add": ""},
{"match": "ਨੀਆਂ", "strip": "ਨੀਆਂ", "add": ""},
{"match": "ਪਣ", "strip": "ਪਣ", "add": ""},
{"match": "ਪਨ", "strip": "ਪਨ", "add": ""},
{"match": "ਪੁਣਾ", "strip": "ਪੁਣਾ", "add": ""},
{"match": "ਪੁੱਣਾ", "strip": "ਪੁੱਣਾ", "add": ""},
{"match": "ਪੁਰ", "strip": "ਪੁਰ", "add": "ਪੁਰ"},
{"match": "ਪੋਸ਼", "strip": "ਪੋਸ਼", "add": ""},
{"match": "ਪੰਥੀ", "strip": "ਪੰਥੀ", "add": ""},
{"match": "ਬਾਜ਼ੀ", "strip": "ਬਾਜ਼ੀ", "add": ""},
{"match": "ਬਾਜੀ", "strip": "ਬਾਜੀ", "add": ""},
{"match": "ਬਾਨ", "strip": "ਬਾਨ", "add": ""},
{"match": "ਬਾਜ", "strip": "ਬਾਜ", "add": ""},
{"match": "ਬੱਧ", "strip": "ਬੱਧ", "add": ""},
{"match": "ਬਾਜ਼", "strip": "ਬਾਜ਼", "add": ""},
{"match": "ਮਾਨ", "strip": "ਮਾਨ", "add": ""},
{"match": "ਮਾਰ", "strip": "ਮਾਰ", "add": ""},
{"match": "ਮੁਖੀ", "strip": "ਮੁਖੀ", "add": ""},
{"match": "ਮੰਦੀ", "strip": "ਮੰਦੀ", "add": ""},
{"match": "ਮੰਦ", "strip": "ਮੰਦ", "add": ""},
{"match": "ਣਗੇ", "strip": "ਣਗੇ", "add": ""},
{"match": "ਣੀਆਂ", "strip": "ਣੀਆਂ", "add": ""},
{"match": "ਯੋਗ", "strip": "ਯੋਗ", "add": ""},
{"match": "ਵਾਂਗਾ", "strip": "ਵਾਂਗਾ", "add": ""},
{"match": "ਵਾਂਗੇ", "strip": "ਵਾਂਗੇ", "add": ""},
{"match": "ਵਾਂਗੀ", "strip": "ਵਾਂਗੀ", "add": ""},
{"match": "ਵੋਗੇ", "strip": "ਵੋਗੇ", "add": ""},
{"match": "ਵੇਗਾ", "strip": "", "add": ""},
{"match": "ਵੇਗੀ", "strip": "ਵੇਗੀ", "add": ""},
{"match": "ਵਟ", "strip": "ਵਟ", "add": ""},
{"match": "ਵਰ", "strip": "ਵਰ", "add": ""},
{"match": "ਵਾਦ", "strip": "ਵਾਦ", "add": ""},
{"match": "ਵਾਨ", "strip": "ਵਾਨ", "add": ""},
{"match": "ਵਾਲਾ", "strip": "ਵਾਲਾ", "add": ""},
{"match": "ਾਵਲੀ", "strip": "ਾਵਲੀ", "add": "ਾਵਲੀ"},
{"match": "ਾਵਟ", "strip": "ਾਵਟ", "add": ""},
{"match": "ਵਟ", "strip": "ਵਟ", "add": ""},
{"match": "ਵਟੀ", "strip": "ਵਟੀ", "add": ""},
{"match": "ਾਵਣ", "strip": "ਵਣ", "add": ""},
{"match": "ਾਵਣੀ", "strip": "ਵਣੀ", "add": ""},
{"match": "ਾਵਣੀ", "strip": "ਣੀ", "add": ""},
{"match": "ਵਾਲ", "strip": "ਵਾਲ", "add": ""},
{"match": "ਵੰਤੀ", "strip": "ਵੰਤੀ", "add": ""},
{"match": "ਵੰਤ", "strip": "ਵੰਤ", "add": ""},
{"match": "ਵੰਦ", "strip": "ਵੰਦ", "add": ""},
{"match": "ਸ਼ਾਹੀ", "strip": "ੀ", "add": ""},
{"match": "ਸ਼ੀਲ", "strip": "ਸ਼ੀਲ", "add": ""},
{"match": "ਸਾਜ", "strip": "ਸਾਜ", "add": ""},
{"match": "ਸਾਜ਼", "strip": "ਸਾਜ਼", "add": ""},
{"match": "ਸਾਰ", "strip": "ਸਾਰ", "add": ""},
{"match": "ਸ਼ਾਲਾ", "strip": "ਸ਼ਾਲਾ", "add": "ਸ਼ਾਲਾ"},
{"match": "ਸਾਲ", "strip": "ਸਾਲ", "add": ""},
{"match": "ਸਾਲ", "strip": "ਸਾਲ", "add": "ਸਾਲ"},
{"match": "ਹਾਰੀ", "strip": "ਹਾਰੀ", "add": ""},
{"match": "ਹਾਰਾ", "strip": "ਹਾਰਾ", "add": ""},
{"match": "ਹਾਰ", "strip": "ਹਾਰ", "add": ""},
{"match": "ਹੀਣ", "strip": "ਹੀਣ", "add": ""},
{"match": "ਹਟ", "strip": "ਹਟ", "add": ""},
{"match": "ਾਹਟ", "strip": "ਾਹਟ", "add": ""},
{"match": "ਿਉਂ", "strip": "ਿਉਂ", "add": "ਾ"},
{"match": "ਿਓਂ", "strip": "ਿਓਂ", "add": "ੇ"},
{"match": "ੀਓ", "strip": "ਓ", "add": ""},
{"match": "ਿਓ", "strip": "ਿਓ", "add": "ਾ/ੀ"},
{"match": "ਿੳ", "strip": "ਿੳ", "add": "ਾ/ੀ"},
{"match": "ਊ", "strip": "ਊ", "add": ""},
{"match": "ਉ", "strip": "ਉ", "add": ""},
{"match": "ਓ", "strip": "ਓ", "add": ""},
{"match": "ੀਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ੀਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ਿਆਂ", "strip": "ਿਆਂ", "add": "ਾ"}, #ਜਾਗਦਿਆਂ
{"match": "ਿਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ਿਆਂ", "strip": "ਿਆਂ", "add": ""}, #ਮੰਗਿਆਂ
{"match": "ੀਆ", "strip": "ਆ", "add": ""},
{"match": "ਿਆ", "strip": "ਿਆ", "add": "ਾ"},
{"match": "ੂਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ੋਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ਆਂ", "strip": "ਆਂ", "add": ""},# ਨਹੁੰਆਂ
{"match": "ਆ", "strip": "ਆ", "add": ""},
{"match": 'ਜੇ', "strip": 'ਜੇ', "add": ""},
{"match": 'ਾਈ', "strip": 'ਈ', "add": ""}, #ਗਹਿਰਾਈ
{"match": 'ਾਈ', "strip": 'ਾਈ', "add": ""},
{"match": 'ਾਈ', "strip": 'ਾਈ', "add": "ਾਈ"}, #ਅਸਥਾਈ
{"match": " ਾਈ", "strip": "ਈ", "add": ""},
{"match": " ਾਈ", "strip": " ਾਈ", "add": ""},
{"match": "ਿਏ", "strip": "ਿਏ", "add": "ੀ"},
{"match": "ਿਏ", "strip": "ਿਏ", "add": ""},
{"match": "ੀਏ", "strip": "ਏ", "add": ""},
 {"match": "ੀਏ", "strip": "ਏ", "add": "ਆ"},# ਏਰੀਏ , ਮੀਡੀਏ
{"match": "ੀਏ", "strip": "ੀਏ", "add": ""}, #ਦੇਖੀਏ
{"match": "ਈਂ", "strip": "ਈਂ", "add": ""},
{"match": "ਈ", "strip": "ਈ", "add": ""},
{"match": "ਿਆਈ", "strip": "ਿਆਈ", "add": "ਾ"}, #ਚੰਗਿਆਈ
{"match": "ਏ", "strip": "ਏ", "add": ""},
{"match": "ਕਾ", "strip": "ਕਾ", "add": ""},
{"match": "ਕੀ", "strip": "ਕੀ", "add": ""},
{"match": "ਕ", "strip": "ਕ", "add": ""},
{"match": "ਕੇ", "strip": "ਕੇ", "add": ""},
{"match": "ਕੇ", "strip": "ੇ", "add": "ਾ"},
{"match": "ਕੇ", "strip": "ਕੇ", "add": "ਕੇ"}, #ਜਾਣਕੇ , ਕਰਕੇ, ਮਿਲਕੇ,  ਕੜਾਕੇ ,ਆਕੇ, ਬਣਾਕੇ, ਬੰਨਕੇ
{"match": "ੇਗੀ", "strip": "ੇਗੀ", "add": ""},
{"match": "ੇਗਾ", "strip": "ੇਗਾ", "add": ""},
{"match": "ੋਗੇ", "strip": "ੋਗੇ", "add": ""},
{"match": "ਾਂਗਾ", "strip": "ਾਂਗਾ", "add": ""},
{"match": "ਾਂਗੀ", "strip": "ਾਂਗੀ", "add": ""},
{"match": "ਾਂਗੇ", "strip": "ਾਂਗੇ", "add": ""},
{"match": "ੋਗੀ", "strip": "ੋਗੀ", "add": ""},#ਕਰੋਗੀ
{"match": "ੋਗੀ", "strip": "ੀ", "add": ""}, #ਯੋਗੀ
{"match": "ਗੀ", "strip": "ਗੀ", "add": ""},
{"match": "ਚੀ", "strip": "ੀ", "add": ""}, #ਸੋਚੀ
{"match": "ਚੀ", "strip": "ਚੀ", "add": "ਚੀ"}, #ਖਜਾਨਚੀ
{"match": "ਾਣੀ", "strip": "ਾਣੀ", "add": "ਾਣੀ"},#ਮਹਾਰਾਣੀ, ਪੁਰਾਣੀ ਪਾਣੀ ਢਾਣੀ ਹਾਣੀ ਖਾਣੀ ਕਹਾਣੀ ਨੌਕਰਾਣੀ
{"match": "ੈਣੀ", "strip": "ਣੀ", "add": ""}, #ਸੈਣੀ
{"match": "ੂਣੀ", "strip": "ੂਣੀ", "add": "ੂਣੀ"}, #ਧੂਣੀ
{"match": "ੁਣੀ", "strip": "ੀ", "add": ""}, #ਸੁਣੀ, ਚੁਣੀ, ਦੋਗੁਣੀ, ਨਿਗੁਣੀ, ਅਣਸੁਣੀ, ਚੌਗੁਣੀ,
{"match": "ੋਣੀ", "strip": "ੀ", "add": ""},
{"match": "ਣੀ", "strip": "ਣੀ", "add": ""},#ਭੁਗਤਣੀ, ਭੇਜਣੀ, ਪੀਣੀ
{"match": "ਣੀ", "strip": "ੀ", "add": ""}, #ਬਣੀ
{"match": "ਣੀ", "strip": "ਣੀ", "add": "ਣੀ"}, #ਕਾਣੀ ਗਿਣੀ
{"match": "ਾਣੇ", "strip": "ੇ", "add": "ਾ"}, #ਥਾਣੇ ਗਾਣੇ ਟਿਕਾਣੇ ਦਾਣੇ
{"match": "ੂਣੇ", "strip": "ੇ", "add": "ਾ"},
{"match": "ੁਣੇ", "strip": "ੇ", "add": ""},
{"match": "ੇਣੇ", "strip": "ੇ", "add": "ਾ"},
{"match": "ੈਣੇ", "strip": "ੇ", "add": ""},
{"match": "ਣੇ", "strip": "ੇ", "add": "ਾ"}, # ਜਾਣੇ, ਸਾਮਣੇ,  ਲਾਣੇ, ਛਣਕਣੇ
{"match": "ਣੇ", "strip": "ਣੇ", "add": ""}, #ਉਠਣੇ
{"match": "ਣਾ", "strip": "ਣਾ", "add": ""},
{"match": "ਣ", "strip": "ਣ", "add": ""},
{"match": "ਤੀ", "strip": "ੀ", "add": ""},
{"match": "ਤੀ", "strip": "ਤੀ", "add": "ਤੀ"},
{"match": "ਤਾ", "strip": "ਤਾ", "add": ""},
{"match": "ਤ", "strip": "ਤ", "add": ""},
{"match": "ਜੀ", "strip": "ਜੀ", "add": ""},
{"match": "ੇ", "strip": "ੇ", "add": "ਾ"},
{"match": "ਾਂਦਾ", "strip": " ਂਦਾ", "add": "ਾ"},
{"match": "ਾਂਦੀ", "strip": "ਾਂਦੀ", "add": "ਾ"},
{"match": " ਾਂਦੇ", "strip": "  ਾਂਦੇ", "add": "ਾ"},
{"match": "ਂਦੇ", "strip": "ਂਦੇ", "add": ""},
{"match": "ਂਦੀ", "strip": "ਂਦੀ", "add": ""},
{"match": "ਂਦਾ", "strip": "ਂਦਾ", "add": ""},
{"match": "ੰਦਾ", "strip": "ੰਦਾ", "add": ""},
{"match": "ੰਦੀ", "strip": "ੰਦੀ", "add": ""},
{"match": "ੰਦੇ", "strip": "ੰਦੇ", "add": ""},
{"match": "ੀਦਾ", "strip": "ੀਦਾ", "add": ""},
{"match": "ਦਾ", "strip": "ਦਾ", "add": ""},
{"match": "ਦੀ", "strip": "ਦੀ", "add": ""},
{"match": "ਦੇ", "strip": "ਦੇ", "add": ""},
{"match": "ਨੀ", "strip": "ਨੀ", "add": "ਨੀ"},
{"match": "ਨਾ", "strip": "ਨਾ", "add": ""},
{"match": "ਨੇ", "strip": "ਨੇ", "add": ""},
{"match": "ਨਾਂ", "strip": "ਨਾਂ", "add": ""},
{"match": "ਨ", "strip": "ਨ", "add": ""},
{"match": "ਪਾ", "strip": "ਪਾ", "add": ""},
{"match": "ਪ", "strip": "ਪ", "add": ""},
{"match": 'ੀਲਾ', "strip": 'ੀਲਾ', "add": ""},
{"match": " ੀਲਾ", "strip": " ੀਲਾ", "add": ""},
{"match": 'ੂਲ਼ਾ', "strip": 'ੂਲ਼ਾ', "add": ""},
{"match": " ੂਲਾ", "strip": " ੂਲਾ", "add": ""},
{"match": " ੂਲਾ", "strip": " ੂਲਾ", "add": ""},
{"match": 'ੇਲੂ', "strip": 'ੇਲੂ', "add": ""},
{"match": "ੈਲ", "strip": "ੈਲ", "add": ""},
{"match": "ਲੂ", "strip": "ਲੂ", "add": ""},
{"match": "ਲਾ", "strip": "ਲਾ", "add": ""},
{"match": "ਲ", "strip": "ਲ", "add": ""},
{"match": "ਵੀ", "strip": "ਵੀ", "add": ""},
{"match": "ਵਾਂ", "strip": "ਵਾਂ", "add": ""},
{"match": "ਵਾ", "strip": "ਵਾ", "add": ""},
{"match": "ਵ", "strip": "ਵ", "add": ""},
{"match": "ਵੇਂ", "strip": "ਵੇਂ", "add": ""},
{"match": "ੜੀ", "strip": "ੜੀ", "add": ""},
{"match": "ੜਾ", "strip": "ੜਾ", "add": ""},
{"match": "ੜ", "strip": "ੜ", "add": ""},
{"match": "ਸ", "strip": "ਸ", "add": "ਸ"},
{"match": "ਸ", "strip": "ਸ", "add": ""},
{"match": " ਾ", "strip": " ਾ", "add": ""},
{"match": 'ਾ', "strip": 'ਾ', "add": ""},
{"match": "ੀਂ", "strip": "ੀਂ", "add": ""},
{"match": " ਿ", "strip": " ਿ", "add": ""},
{"match": "ੀ", "strip": "ੀ", "add": ""},
{"match": "ੀ", "strip":"ੀ", "add": "ੀ"},
{"match": 'ਿ', "strip": 'ਿ', "add": ""},
{"match": 'ੀ', "strip": 'ੀ', "add": ""},
{"match": 'ੁ', "strip": 'ੁ', "add": ""},
{"match": 'ੂ', "strip": 'ੂ', "add": ""},
{"match": " ੂ", "strip": " ੂ", "add": ""},
{"match": "ਾਂ", "strip": "ਾਂ", "add": ""},
{"match": "ੋ", "strip": "ੋ", "add": ""},
{"match": "ੋਂ", "strip": "ੋਂ", "add": ""},
{"match": "ੋ ਂ", "strip": "ੋ ਂ", "add": ""}
```
## Contributing
Contributions to punjabi_stopwords are welcome! If you have suggestions for additional stopwords, or improvements to the existing list, please feel free to contribute.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
